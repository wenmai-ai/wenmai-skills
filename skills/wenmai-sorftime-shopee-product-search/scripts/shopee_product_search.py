#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_product_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_product_search.py',
        path='/sorftime/shopee-product-search',
        required_fields=['site'],
        sample_params={'site': 'TH'},
    )
