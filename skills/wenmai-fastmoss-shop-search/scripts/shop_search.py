#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `shop_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="shop_search.py",
        path="fastmoss/shop-search",
        required_fields=[],
        sample_params={},
    )
