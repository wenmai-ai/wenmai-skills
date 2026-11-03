#!/usr/bin/env python3
"""Call one fixed Wenmai YY standard API endpoint: 获取已抓取的评论."""

from _review_rules import check_aids
from _wenmai_api import load_params, call_standard_api
import json

SAMPLE = {"aids": [67124951]}

if __name__ == "__main__":
    params = load_params("get_monitor_asin_reviews.py", SAMPLE)
    check_aids(params)
    result = call_standard_api(params=params, path="/yy/get-monitor-asin-reviews", required_fields=["aids"])
    print(json.dumps(result, ensure_ascii=False, indent=2))
