#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_ozon_scraper_pro.py',
        path='/alpha/ozon-scraper-pro',
        required_fields=[],
        sample_params={'urls': ['https://www.ozon.ru/category/noutbuki-15692/'], 'onSale': False, 'queries': ['iphone', 'samsung galaxy'], 'sorting': 'score', 'currency': 'RUB', 'language': 'ru', 'maxPrice': 3, 'minPrice': 1, 'maxResults': 3, 'hasDiscount': False, 'skipDetails': False, 'isInstallment': False, 'brandCertified': False, 'hasReviewPoints': False, 'includeSellerDetails': False},
    )
