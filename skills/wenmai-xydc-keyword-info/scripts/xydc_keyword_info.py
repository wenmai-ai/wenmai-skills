#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_keyword_info.py',
        path='/xydc/get-keyword-info',
        required_fields=['country', 'keywords'],
        sample_params={'keywords': ['usb c cable'], 'country': 'US'},
    )
