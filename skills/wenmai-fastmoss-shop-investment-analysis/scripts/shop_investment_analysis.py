#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `shop_investment_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="shop_investment_analysis.py",
        path="fastmoss/shop-investment-analysis",
        required_fields=['filter', 'filter.seller_id', 'filter.date_info'],
        sample_params={'filter': {'seller_id': 'example-id', 'date_info': {}}},
    )
