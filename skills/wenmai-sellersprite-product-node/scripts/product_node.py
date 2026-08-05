#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `product_node` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_node.py',
        path='/sellersprite/product-node',
        required_fields=['request', 'request.marketplace'],
        sample_params={'request': {'marketplace': 'US'}},
    )
