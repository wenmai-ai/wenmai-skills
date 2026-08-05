#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `ali1688_similar_product` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ali1688_similar_product.py',
        path='/sorftime/ali1688-similar-product',
        required_fields=['search_name'],
        sample_params={'search_name': 'wireless earbuds'},
    )
