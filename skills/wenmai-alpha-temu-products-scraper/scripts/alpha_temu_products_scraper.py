#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_temu_products_scraper.py',
        path='/alpha/temu-products-scraper',
        required_fields=['searchQueries'],
        sample_params={'currency': 'USD', 'maxResults': 40, 'searchQueries': ['women dress']},
    )
