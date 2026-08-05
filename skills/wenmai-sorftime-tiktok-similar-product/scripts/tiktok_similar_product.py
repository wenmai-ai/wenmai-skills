#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `tiktok_similar_product` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tiktok_similar_product.py',
        path='/sorftime/tiktok-similar-product',
        required_fields=['product_name', 'site'],
        sample_params={'product_name': 'wireless earbuds', 'site': 'US'},
    )
