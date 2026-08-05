#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `similar_product_feature` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='similar_product_feature.py',
        path='/sorftime/similar-product-feature',
        required_fields=['product_name', 'amz_site'],
        sample_params={'product_name': 'wireless earbuds', 'amz_site': 'US'},
    )
