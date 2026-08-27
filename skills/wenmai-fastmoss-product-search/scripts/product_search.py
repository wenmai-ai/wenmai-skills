#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_search.py",
        path="fastmoss/product-search",
        required_fields=[],
        sample_params={},
    )
