#!/usr/bin/env python3
"""Call one fixed Wenmai SellerSprite standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='traffic_source.py',
        path='/sellersprite/traffic-source',
        required_fields=['request', 'request.marketplace', 'request.q', 'request.month'],
        sample_params={'request': {'marketplace': 'US', 'q': 'B08GHW4TBS', 'month': '202203'}},
    )
