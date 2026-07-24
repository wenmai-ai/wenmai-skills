#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_asin_keyword_rank_hourly.py',
        path='/xydc/get-asin-keyword-rank-hourly',
        required_fields=['asin', 'country', 'date', 'keyword'],
        sample_params={'asin': 'B09PCSR9SX', 'keyword': 'neck fan', 'country': 'US', 'date': '2026-06-01'},
    )
