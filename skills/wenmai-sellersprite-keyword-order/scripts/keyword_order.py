#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `keyword_order` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_order.py',
        path='/sellersprite/keyword-order',
        required_fields=['request', 'request.marketplace', 'request.asins', 'request.reverseType'],
        sample_params={'request': {'date': '2026-03-29', 'asins': ['B08GHW4TBS'], 'marketplace': 'US', 'reverseType': 'W'}},
    )
