#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_newegg_product_scraper.py',
        path='/alpha/newegg-product-scraper',
        required_fields=[],
        sample_params={'keywords': ['RTX 4070'], 'maxItems': 3, 'maxPages': 3, 'productUrls': ['https://www.newegg.com/p/pl?d=Laptop'], 'requestTimeoutSecs': 30},
    )
