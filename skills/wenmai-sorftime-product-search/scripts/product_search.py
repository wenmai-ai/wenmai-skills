#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_search.py',
        path='/sorftime/product-search',
        required_fields=['amz_site'],
        sample_params={'amz_site': 'US'},
    )
