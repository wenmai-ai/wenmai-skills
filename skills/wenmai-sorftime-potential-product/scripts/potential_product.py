#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `potential_product` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='potential_product.py',
        path='/sorftime/potential-product',
        required_fields=['amz_site'],
        sample_params={'amz_site': 'US'},
    )
