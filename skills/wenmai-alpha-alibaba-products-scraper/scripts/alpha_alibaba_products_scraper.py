#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_alibaba_products_scraper.py',
        path='/alpha/alibaba-products-scraper',
        required_fields=['queries'],
        sample_params={'moq_min': 1, 'queries': ['wireless earbuds'], 'max_pages': 1, 'price_max': 1, 'price_min': 1, 'start_page': 1, 'trade_assurance': False, 'verified_supplier': False, 'alibaba_guaranteed': False},
    )
