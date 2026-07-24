#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_asin_info.py',
        path='/xydc/get-asin-info',
        required_fields=['asins', 'country'],
        sample_params={'asins': ['B09PCSR9SX'], 'country': 'US'},
    )
