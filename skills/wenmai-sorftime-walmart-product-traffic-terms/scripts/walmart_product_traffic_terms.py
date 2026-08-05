#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_product_traffic_terms` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_product_traffic_terms.py',
        path='/sorftime/walmart-product-traffic-terms',
        required_fields=['product_id'],
        sample_params={'product_id': '11381374703'},
    )
