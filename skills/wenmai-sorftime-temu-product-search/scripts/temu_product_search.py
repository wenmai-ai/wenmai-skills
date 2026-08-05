#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `temu_product_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='temu_product_search.py',
        path='/sorftime/temu-product-search',
        required_fields=['site'],
        sample_params={'site': 'US'},
    )
