#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `shop_rank_top_selling` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="shop_rank_top_selling.py",
        path="fastmoss/shop-rank-top-selling",
        required_fields=['filter.date_type', 'filter.date_value', 'filter.date_info'],
        sample_params={'filter': {'date_type': 1, 'date_value': 'example', 'date_info': {}}},
    )
