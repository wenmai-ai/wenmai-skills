#!/usr/bin/env python3
"""YY review crawl in one run: submit one ASIN, poll the task until has_rel=2, then fetch its reviews.

Usage:
  crawl_reviews.py '<add-review-monitor-asins JSON>' ['<review filter JSON>']
  crawl_reviews.py --aid <task id> ['<review filter JSON>']      # resume an already submitted task, no new charge

The optional review filter accepts the documented get-monitor-asin-reviews fields except aids:
review_date_start, review_date_end, star_start, star_end.
Prints one JSON object with the raw responses of every step; progress goes to stderr.
Exit codes: 0 reviews fetched, 3 still crawling when the wait limit was reached (resume with --aid), 1 error.
"""

import json
import os
import sys
import time

from _review_rules import STATIONS, check_add
from _wenmai_api import call_standard_api, die

FILTER_FIELDS = {"review_date_start", "review_date_end", "star_start", "star_end"}
SAMPLE = {"station": "1", "asins": ["B085DTZQNZ"], "review_end_num": 2}


def seconds(name: str, default: int) -> int:
    raw = os.environ.get(name, str(default))
    try:
        value = int(raw)
    except ValueError:
        die(f"{name} must be an integer number of seconds.")
    if value <= 0:
        die(f"{name} must be greater than 0.")
    return value


def parse_json(raw: str, what: str) -> dict:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Invalid {what} JSON: {exc}")
    if not isinstance(value, dict):
        die(f"{what} must be a JSON object.")
    return value


def ok(response: dict) -> bool:
    return isinstance(response, dict) and response.get("code") == "OK"


def first_result(response: dict) -> dict:
    result = (response.get("data") or {}).get("result") if isinstance(response, dict) else None
    return result[0] if isinstance(result, list) and result and isinstance(result[0], dict) else {}


def finish(output: dict, code: int) -> None:
    print(json.dumps(output, ensure_ascii=False, indent=2))
    sys.exit(code)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        die("Usage: crawl_reviews.py '<add JSON>' ['<review filter JSON>'] | crawl_reviews.py --aid <id> ['<filter JSON>']\n"
            f"Example: crawl_reviews.py '{json.dumps(SAMPLE)}'")
    output = {"status": None, "aid": None}
    if args[0] == "--aid":
        if len(args) < 2 or not args[1].isdigit():
            die("--aid requires the integer task id returned by add_review_monitor_asins.py.")
        aid, rest = int(args[1]), args[2:]
    else:
        submit = parse_json(args[0], "add-review-monitor-asins")
        check_add(submit)
        rest = args[1:]
        response = call_standard_api(params=submit, path="/yy/add-review-monitor-asins",
                                     required_fields=["station", "asins"], enum_fields={"station": STATIONS})
        output["submit"] = response
        item = first_result(response)
        if not ok(response) or not isinstance(item.get("aid"), int) or str(item.get("status")).lower() != "true":
            output["status"] = "submit_failed"
            finish(output, 1)
        aid = item["aid"]
        print(f"submitted aid={aid} costCredit={response.get('costCredit')} requestId={response.get('requestId')}", file=sys.stderr)
    output["aid"] = aid
    review_filter = parse_json(rest[0], "review filter") if rest else {}
    unknown = set(review_filter) - FILTER_FIELDS
    if unknown:
        die("Unsupported review filter field(s): " + ", ".join(sorted(unknown)) + "; allowed: " + ", ".join(sorted(FILTER_FIELDS)))

    poll, wait = seconds("WENMAI_REVIEW_POLL_SECONDS", 30), seconds("WENMAI_REVIEW_WAIT_SECONDS", 600)
    started, polls = time.monotonic(), 0
    while True:
        response = call_standard_api(params={"aids": [aid]}, path="/yy/get-review-monitor-tasks", required_fields=["aids"])
        polls += 1
        output["task"] = response
        task = first_result(response)
        if not ok(response):
            output["status"], output["polls"] = "task_query_failed", polls
            finish(output, 1)
        elapsed = int(time.monotonic() - started)
        print(f"poll#{polls} has_rel={task.get('has_rel')} page_num={task.get('page_num')} elapsed={elapsed}s", file=sys.stderr)
        if task.get("has_rel") is None and not task.get("asin"):
            # YY answers an unknown aid with an empty task: only id and task_status are set.
            output.update(status="task_not_found", polls=polls,
                          hint=f"aid {aid} is not a review task of this account; check the id returned by the submit step.")
            finish(output, 1)
        if task.get("has_rel") == 2:
            break
        if elapsed + poll > wait:
            output.update(status="still_crawling", polls=polls, elapsedSeconds=elapsed,
                          hint=f"Task {aid} is still queued or crawling. Resume later with: crawl_reviews.py --aid {aid}")
            finish(output, 3)
        time.sleep(poll)

    response = call_standard_api(params={"aids": [aid], **review_filter}, path="/yy/get-monitor-asin-reviews",
                                 required_fields=["aids"])
    output["reviews"] = response
    output["polls"], output["elapsedSeconds"] = polls, int(time.monotonic() - started)
    output["status"] = "done" if ok(response) else "reviews_query_failed"
    finish(output, 0 if ok(response) else 1)


if __name__ == "__main__":
    main()
