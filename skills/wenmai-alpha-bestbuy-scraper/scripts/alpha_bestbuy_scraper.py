#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_bestbuy_scraper.py',
        path='/alpha/bestbuy-scraper',
        required_fields=['searchQuery'],
        sample_params={'zipCode': '10001', 'maxResults': 3, 'searchQuery': 'laptop', 'fetchProductDetails': True},
    )
