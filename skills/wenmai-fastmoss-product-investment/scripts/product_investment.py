#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_investment` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_investment.py",
        path="fastmoss/product-investment",
        required_fields=['filter', 'filter.product_id', 'filter.date_info'],
        sample_params={'filter': {'product_id': 'example-id', 'date_info': {}}},
    )
