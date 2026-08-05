#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_category_request` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_category_request.py',
        path='/sorftime/shopee-category-request',
        required_fields=['node_id', 'site'],
        sample_params={'node_id': '1055398', 'site': 'TH'},
    )
