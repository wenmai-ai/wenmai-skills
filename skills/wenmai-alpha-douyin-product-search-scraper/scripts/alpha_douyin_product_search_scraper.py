#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_douyin_product_search_scraper.py',
        path='/alpha/douyin-product-search-scraper',
        required_fields=['keywords'],
        sample_params={'keywords': ['口红'], 'maxResults': 3},
    )
