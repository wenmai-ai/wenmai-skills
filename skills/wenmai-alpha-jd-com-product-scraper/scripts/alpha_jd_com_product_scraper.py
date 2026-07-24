#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_jd_com_product_scraper.py',
        path='/alpha/jd-com-product-scraper',
        required_fields=[],
        sample_params={'itemId': '100256400499', 'shopId': '1000004259', 'keyword': '华为手机', 'maxPages': 3, 'operation': 'productSearch'},
    )
