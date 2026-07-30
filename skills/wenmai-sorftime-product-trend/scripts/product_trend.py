#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_trend.py',
        path='/sorftime/product-trend',
        required_fields=['asin', 'amz_site'],
        sample_params={'asin': 'B0CZPLV566', 'amz_site': 'US'},
    )
