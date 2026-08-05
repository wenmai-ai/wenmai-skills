#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `market_product_demand_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='market_product_demand_trend.py',
        path='/sellersprite/market-product-demand-trend',
        required_fields=['request', 'request.marketplace', 'request.nodeIdPath'],
        sample_params={'request': {'nodeIdPath': '172282:281407', 'marketplace': 'US'}},
    )
