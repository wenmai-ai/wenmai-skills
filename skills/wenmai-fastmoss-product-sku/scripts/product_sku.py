#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_sku` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_sku.py",
        path="fastmoss/product-sku",
        required_fields=['filter', 'filter.product_id'],
        sample_params={'filter': {'product_id': 'example-id'}},
    )
