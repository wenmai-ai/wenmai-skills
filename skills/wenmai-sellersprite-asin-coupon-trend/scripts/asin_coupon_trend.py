#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `asin_coupon_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='asin_coupon_trend.py',
        path='/sellersprite/asin-coupon-trend',
        required_fields=['marketplace', 'asin'],
        sample_params={'asin': 'B08GHW4TBS', 'marketplace': 'US'},
    )
