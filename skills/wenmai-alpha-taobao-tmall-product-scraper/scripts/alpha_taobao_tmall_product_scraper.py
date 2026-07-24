#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_taobao_tmall_product_scraper.py',
        path='/alpha/taobao-tmall-product-scraper',
        required_fields=[],
        sample_params={'sort': '_sale', 'itemId': '744983869996', 'shopId': '67095450', 'userId': '713464357', 'keyword': 'iphone 15', 'endPrice': 5000, 'maxPages': 3, 'operation': 'keywordSearch', 'orderType': 'feedbackdate', 'tmallOnly': False, 'startPrice': 100, 'detailVersion': 'v9', 'catalogVersion': 'v1'},
    )
