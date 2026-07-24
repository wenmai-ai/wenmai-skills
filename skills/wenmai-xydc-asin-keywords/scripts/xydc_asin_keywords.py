#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_asin_keywords.py',
        path='/xydc/get-asin-keywords',
        required_fields=['asin', 'country'],
        sample_params={'asin': 'B09PCSR9SX', 'country': 'US', 'page': 1, 'page_size': 20},
    )
