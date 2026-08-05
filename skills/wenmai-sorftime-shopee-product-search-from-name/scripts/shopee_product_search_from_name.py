#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_product_search_from_name` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_product_search_from_name.py',
        path='/sorftime/shopee-product-search-from-name',
        required_fields=['name', 'site'],
        sample_params={'name': 'wireless earbuds', 'site': 'TH'},
    )
