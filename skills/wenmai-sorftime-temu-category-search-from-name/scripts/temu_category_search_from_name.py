#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `temu_category_search_from_name` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='temu_category_search_from_name.py',
        path='/sorftime/temu-category-search-from-name',
        required_fields=['name', 'site'],
        sample_params={'name': 'wireless earbuds', 'site': 'US'},
    )
