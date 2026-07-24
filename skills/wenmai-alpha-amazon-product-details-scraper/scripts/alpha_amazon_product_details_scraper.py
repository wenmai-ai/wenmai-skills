#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_amazon_product_details_scraper.py',
        path='/alpha/amazon-product-details-scraper',
        required_fields=['Params'],
        sample_params={'Params': ['B00091S3K4', 'https://www.amazon.com/dp/B077Z99YGY']},
    )
