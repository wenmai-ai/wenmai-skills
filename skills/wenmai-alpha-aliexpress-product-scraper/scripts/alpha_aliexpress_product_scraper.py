#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_aliexpress_product_scraper.py',
        path='/alpha/aliexpress-product-scraper',
        required_fields=[],
        sample_params={'sortBy': 'default', 'country': 'US', 'queries': ['bluetooth earbuds'], 'category': 'all', 'maxPrice': 1, 'minPrice': 1, 'trending': False, 'maxResults': 3, 'subcategorySlug': 'keyboard'},
    )
