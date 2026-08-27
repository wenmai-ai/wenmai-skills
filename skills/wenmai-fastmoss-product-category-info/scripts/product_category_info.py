#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_category_info` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_category_info.py",
        path="fastmoss/product-category-info",
        required_fields=[],
        sample_params={},
    )
