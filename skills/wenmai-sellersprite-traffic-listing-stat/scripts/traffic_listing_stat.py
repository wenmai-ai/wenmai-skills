#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `traffic_listing_stat` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='traffic_listing_stat.py',
        path='/sellersprite/traffic-listing-stat',
        required_fields=['marketplace'],
        sample_params={'asin': 'B08GHW4TBS', 'marketplace': 'US'},
    )
