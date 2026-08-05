#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `keyword_miner` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_miner.py',
        path='/sellersprite/keyword-miner',
        required_fields=['request', 'request.marketplace', 'request.keyword'],
        sample_params={'request': {'keyword': 'wireless earbuds', 'marketplace': 'US'}},
    )
