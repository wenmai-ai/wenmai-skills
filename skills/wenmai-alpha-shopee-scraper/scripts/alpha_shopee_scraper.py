#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_shopee_scraper.py',
        path='/alpha/shopee-scraper',
        required_fields=[],
        sample_params={'debug': False, 'country': 'SG', 'keywords': ['phone case'], 'maxItems': 10, 'priceSlicing': False},
    )
