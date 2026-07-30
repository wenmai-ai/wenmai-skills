#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_search_from_history` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_search_from_history.py',
        path='/sorftime/product-search-from-history',
        required_fields=['search_time', 'amz_site'],
        sample_params={'search_time': '2026-06', 'amz_site': 'US'},
    )
