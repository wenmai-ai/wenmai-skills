#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_product_trend_by_product_id` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_product_trend_by_product_id.py',
        path='/sorftime/walmart-product-trend-by-product-id',
        required_fields=['product_id'],
        sample_params={'product_id': '11381374703'},
    )
