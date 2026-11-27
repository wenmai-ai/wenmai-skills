#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='marketplace_item.py',
        path='/scrapecreators/facebook-marketplace-item',
        required_fields=[],
        sample_params={'id': '1234567890'},
    )
