#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_wildberries_products_search_scraper.py',
        path='/alpha/wildberries-products-search-scraper',
        required_fields=['searchUrl'],
        sample_params={'maxItems': 3, 'searchUrl': 'https://www.wildberries.ru/catalog/0/search.aspx?search=iphone'},
    )
