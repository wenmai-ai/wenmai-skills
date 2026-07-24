#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_jumia_product_search_scraper.py',
        path='/alpha/jumia-product-search-scraper',
        required_fields=[],
        sample_params={'urls': ['https://www.jumia.com.ng/catalog/?q=shoe&page=11#catalog-listing'], 'max_items_per_url': 3, 'ignore_url_failures': True},
    )
