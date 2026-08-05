#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_keyword_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_keyword_search.py',
        path='/sorftime/shopee-keyword-search',
        required_fields=['site'],
        sample_params={'site': 'TH'},
    )
