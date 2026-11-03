#!/usr/bin/env python3
"""Call one fixed Wenmai YY standard API endpoint: 查询评论任务抓取次数."""

from _review_rules import check_aids
from _wenmai_api import load_params, call_standard_api
import json

SAMPLE = {"aids": [67124951]}

if __name__ == "__main__":
    params = load_params("get_review_crawl_count.py", SAMPLE)
    check_aids(params)
    result = call_standard_api(params=params, path="/yy/get-review-crawl-count", required_fields=["aids"])
    print(json.dumps(result, ensure_ascii=False, indent=2))
