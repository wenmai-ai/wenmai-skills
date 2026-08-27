#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_sales_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_sales_trend.py",
        path="fastmoss/product-sales-trend",
        required_fields=['filter.product_id', 'filter.time_range_days', 'filter.days'],
        sample_params={'filter': {'product_id': 'example-id', 'time_range_days': 1, 'days': 1}},
    )
