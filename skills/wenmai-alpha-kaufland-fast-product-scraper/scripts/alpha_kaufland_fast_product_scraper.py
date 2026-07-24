#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_kaufland_fast_product_scraper.py',
        path='/alpha/kaufland-fast-product-scraper',
        required_fields=[],
        sample_params={'keyword': 'keyboard', 'startUrlsCategories': [{'url': 'https://www.kaufland.de/c/badausstattung/~27721/'}], 'maxProductsPerCategory': 3},
    )
