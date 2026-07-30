#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_traffic_terms` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_traffic_terms.py',
        path='/sorftime/product-traffic-terms',
        required_fields=['asin', 'amz_site'],
        sample_params={'asin': 'B0CZPLV566', 'amz_site': 'US'},
    )
