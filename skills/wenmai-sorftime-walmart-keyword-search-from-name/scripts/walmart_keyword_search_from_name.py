#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_keyword_search_from_name` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_keyword_search_from_name.py',
        path='/sorftime/walmart-keyword-search-from-name',
        required_fields=['name'],
        sample_params={'name': 'wireless earbuds'},
    )
