#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_walmart_fast_product_scraper.py',
        path='/alpha/walmart-fast-product-scraper',
        required_fields=['startUrls'],
        sample_params={'startUrls': [{'url': 'https://walmart.com/search?q=tshirt'}], 'maxProductsPerStartUrl': 3},
    )
