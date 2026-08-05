#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `temu_product_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='temu_product_trend.py',
        path='/sorftime/temu-product-trend',
        required_fields=['product_id', 'site'],
        sample_params={'product_id': '601099557680075', 'site': 'US'},
    )
