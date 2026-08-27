#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_review_list` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_review_list.py",
        path="fastmoss/product-review-list",
        required_fields=['filter.product_id'],
        sample_params={'filter': {'product_id': 'example-id'}},
    )
