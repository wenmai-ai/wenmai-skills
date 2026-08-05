#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `traffic_extend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='traffic_extend.py',
        path='/sellersprite/traffic-extend',
        required_fields=['request', 'request.marketplace', 'request.asinList'],
        sample_params={'request': {'asinList': ['B08GHW4TBS'], 'queryType': 1, 'marketplace': 'US'}},
    )
