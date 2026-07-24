#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_keyword_aba_trends.py',
        path='/xydc/get-keyword-aba-trends',
        required_fields=['country', 'end_week', 'keywords', 'start_week'],
        sample_params={'keywords': ['usb c cable'], 'country': 'US', 'start_week': '2026-06-01', 'end_week': '2026-06-07'},
    )
