#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_shopify_product_scraper.py',
        path='/alpha/shopify-product-scraper',
        required_fields=[],
        sample_params={'mode': 'url', 'maxPages': 1, 'storeUrls': [{'url': 'https://www.allbirds.com'}], 'maxProducts': 20},
    )
