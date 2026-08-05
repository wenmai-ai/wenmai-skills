#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `market_listing_trend_distribution` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='market_listing_trend_distribution.py',
        path='/sellersprite/market-listing-trend-distribution',
        required_fields=['request'],
        sample_params={'request': {'nodeIdPath': '172282:281407', 'marketplace': 'US'}},
    )
