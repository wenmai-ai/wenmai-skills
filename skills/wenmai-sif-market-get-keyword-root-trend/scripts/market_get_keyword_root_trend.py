#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `market_get_keyword_root_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='market_get_keyword_root_trend.py',
        path='/sif/market-get-keyword-root-trend',
        required_fields=['keyword'],
        sample_params={'keyword': 'wireless earbuds'},
    )
