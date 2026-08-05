#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ops_get_asin_traffic_trend_detail` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ops_get_asin_traffic_trend_detail.py',
        path='/sif/ops-get-asin-traffic-trend-detail',
        required_fields=['asin', 'endDay', 'granularity', 'desc', 'pageNum', 'pageSize'],
        sample_params={'asin': 'B08GHW4TBS', 'desc': False, 'endDay': '2026-03-29', 'pageNum': 1, 'pageSize': 1, 'granularity': 'day'},
    )
