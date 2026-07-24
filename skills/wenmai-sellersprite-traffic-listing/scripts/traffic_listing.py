#!/usr/bin/env python3
"""Call one fixed Wenmai SellerSprite standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='traffic_listing.py',
        path='/sellersprite/traffic-listing',
        required_fields=['request', 'request.marketplace', 'request.asinList', 'request.relations'],
        sample_params={'request': {'asinList': ['B08GHW4TBS'], 'marketplace': 'US', 'relations': ['vav']}},
    )
