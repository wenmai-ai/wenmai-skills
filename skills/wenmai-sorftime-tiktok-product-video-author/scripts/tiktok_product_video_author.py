#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `tiktok_product_video_author` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tiktok_product_video_author.py',
        path='/sorftime/tiktok-product-video-author',
        required_fields=['product_id', 'site'],
        sample_params={'product_id': '1732349647191642367', 'site': 'US'},
    )
