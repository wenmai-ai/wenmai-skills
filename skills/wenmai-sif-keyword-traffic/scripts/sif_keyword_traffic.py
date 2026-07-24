#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sif_keyword_traffic.py',
        path='/sif/market-get-keyword-competition',
        required_fields=['keyword'],
        sample_params={'keyword': 'wireless earbuds', 'country': 'US', 'time_type': 'all', 'rank_evolution': False},
    )
