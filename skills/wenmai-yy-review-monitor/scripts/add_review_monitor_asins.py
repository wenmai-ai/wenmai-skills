#!/usr/bin/env python3
"""Call one fixed Wenmai YY standard API endpoint: submit one ASIN for review crawling."""

from _review_rules import STATIONS, check_add
from _wenmai_api import load_params, call_standard_api
import json

SAMPLE = {"station": "1", "asins": ["B085DTZQNZ"], "review_end_num": 2}

if __name__ == "__main__":
    params = load_params("add_review_monitor_asins.py", SAMPLE)
    check_add(params)
    result = call_standard_api(params=params, path="/yy/add-review-monitor-asins",
                               required_fields=["station", "asins"], enum_fields={"station": STATIONS})
    print(json.dumps(result, ensure_ascii=False, indent=2))
