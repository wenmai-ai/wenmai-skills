#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_keyword_analysis_monthly.py',
        path='/xydc/get-keyword-analysis-monthly',
        required_fields=['country', 'end_month', 'keyword', 'start_month'],
        sample_params={'keyword': 'usb c cable', 'country': 'US', 'start_month': '2026-05', 'end_month': '2026-06', 'page': 1, 'page_size': 20},
    )
