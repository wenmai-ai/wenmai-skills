#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `temu_shop_request` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='temu_shop_request.py',
        path='/sorftime/temu-shop-request',
        required_fields=['shop_id', 'site'],
        sample_params={'shop_id': '16197192', 'site': 'US'},
    )
