#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_free_amazon_product_scraper.py',
        path='/alpha/free-amazon-product-scraper',
        required_fields=['categoryUrls'],
        sample_params={'categoryUrls': [{'url': 'https://www.amazon.com/s?k=keyboard'}], 'useCaptchaSolver': False, 'maxItemsPerStartUrl': 3, 'scrapeProductDetails': True, 'maxSearchPagesPerStartUrl': 3, 'scrapeProductVariantPrices': False, 'maxProductVariantsAsSeparateResults': 0},
    )
