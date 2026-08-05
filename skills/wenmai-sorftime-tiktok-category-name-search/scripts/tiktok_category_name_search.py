#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `tiktok_category_name_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tiktok_category_name_search.py',
        path='/sorftime/tiktok-category-name-search',
        required_fields=['search_name', 'site'],
        sample_params={'search_name': 'wireless earbuds', 'site': 'US'},
    )
