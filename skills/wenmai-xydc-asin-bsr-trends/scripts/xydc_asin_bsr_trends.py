#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_asin_bsr_trends.py',
        path='/xydc/get-asin-bsr-trends',
        required_fields=['asin', 'country', 'end_date', 'start_date'],
        sample_params={'asin': 'B09PCSR9SX', 'country': 'US', 'start_date': '2026-06-01', 'end_date': '2026-06-07'},
    )
