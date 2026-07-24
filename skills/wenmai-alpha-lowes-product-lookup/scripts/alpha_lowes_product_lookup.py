#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_lowes_product_lookup.py',
        path='/alpha/lowes-product-lookup',
        required_fields=[],
        sample_params={'zip': '10918', 'productId': '3131025'},
    )
