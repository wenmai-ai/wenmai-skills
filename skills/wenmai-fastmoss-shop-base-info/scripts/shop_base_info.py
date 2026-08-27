#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `shop_base_info` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="shop_base_info.py",
        path="fastmoss/shop-base-info",
        required_fields=['filter', 'filter.seller_id'],
        sample_params={'filter': {'seller_id': 'example-id'}},
    )
