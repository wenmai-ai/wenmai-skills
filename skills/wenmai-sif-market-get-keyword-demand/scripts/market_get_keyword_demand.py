#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `market_get_keyword_demand` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='market_get_keyword_demand.py',
        path='/sif/market-get-keyword-demand',
        required_fields=['keywords'],
        sample_params={'keywords': ['wireless earbuds']},
    )
