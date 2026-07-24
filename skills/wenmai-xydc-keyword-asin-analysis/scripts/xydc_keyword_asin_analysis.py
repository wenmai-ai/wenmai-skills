#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_keyword_asin_analysis.py',
        path='/xydc/get-keyword-asin-analysis',
        required_fields=['country', 'keyword'],
        sample_params={'keyword': 'usb c cable', 'country': 'US', 'page': 1, 'page_size': 20},
    )
