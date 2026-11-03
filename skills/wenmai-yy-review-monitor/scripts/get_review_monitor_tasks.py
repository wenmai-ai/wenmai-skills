#!/usr/bin/env python3
"""Call one fixed Wenmai YY standard API endpoint: 查询评论任务状态."""

from _review_rules import check_aids
from _wenmai_api import load_params, call_standard_api
import json

SAMPLE = {"aids": [67124951]}

if __name__ == "__main__":
    params = load_params("get_review_monitor_tasks.py", SAMPLE)
    check_aids(params)
    result = call_standard_api(params=params, path="/yy/get-review-monitor-tasks", required_fields=["aids"])
    print(json.dumps(result, ensure_ascii=False, indent=2))
