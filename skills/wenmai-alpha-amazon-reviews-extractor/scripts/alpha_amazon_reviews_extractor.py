#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_amazon_reviews_extractor.py',
        path='/alpha/amazon-reviews-extractor',
        required_fields=['products'],
        sample_params={'sort': 'helpful', 'limit': 3, 'rating': 'all', 'region': 'amazon.com', 'keywords': ['keyboard'], 'language': 'all', 'products': ['https://www.amazon.com/Logitech-LIGHTSPEED-Wireless-Gaming-Mouse/product-reviews/B07CMS5Q6P/ref=cm_cr_getr_mb_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2&formatType=current_format', 'B07MVJZQTC'], 'all_stars': False, 'avp_reviews': False, 'personal_data': False, 'include_variants': True, 'scrape_image_reviews': True, 'scrape_video_reviews': True},
    )
