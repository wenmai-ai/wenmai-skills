#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sif_keyword_overview.py',
        path='/sif/market-get-keyword-history',
        required_fields=['keywords'],
        sample_params={'keywords': ['wireless earbuds'], 'country': 'US', 'granularity': 'week'},
    )
