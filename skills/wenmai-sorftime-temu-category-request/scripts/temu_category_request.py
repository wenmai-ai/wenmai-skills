#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `temu_category_request` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='temu_category_request.py',
        path='/sorftime/temu-category-request',
        required_fields=['node_id', 'site'],
        sample_params={'node_id': '248', 'site': 'US'},
    )
