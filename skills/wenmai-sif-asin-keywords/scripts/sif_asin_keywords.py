#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sif_asin_keywords.py',
        path='/sif/market-get-asin-keyword-signals',
        required_fields=['asin'],
        sample_params={'asin': 'B08GHW4TBS', 'country': 'US', 'time_type': 'lately', 'time_value': '7', 'topN': 50},
    )
