#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `ali1688_product_request` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ali1688_product_request.py',
        path='/sorftime/ali1688-product-request',
        required_fields=['product_id'],
        sample_params={'product_id': '789542752062'},
    )
