#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_name_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_name_search.py',
        path='/sorftime/category-name-search',
        required_fields=['category_name', 'amz_site'],
        sample_params={'category_name': 'Home & Kitchen', 'amz_site': 'US'},
    )
