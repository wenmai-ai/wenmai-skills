#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_search_from_product_name` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_search_from_product_name.py',
        path='/sorftime/category-search-from-product-name',
        required_fields=['product_name', 'amz_site'],
        sample_params={'product_name': 'wireless earbuds', 'amz_site': 'US'},
    )
