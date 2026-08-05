#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `keepa_info` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keepa_info.py',
        path='/sellersprite/keepa-info',
        required_fields=['marketplace', 'asin'],
        sample_params={'asin': 'B08GHW4TBS', 'marketplace': 'US'},
    )
