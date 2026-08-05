#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `search_categories_broadly` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_categories_broadly.py',
        path='/sorftime/search-categories-broadly',
        required_fields=['amz_site'],
        sample_params={'amz_site': 'US'},
    )
