#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `shop_video_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="shop_video_analysis.py",
        path="fastmoss/shop-video-analysis",
        required_fields=['filter', 'filter.seller_id'],
        sample_params={'filter': {'seller_id': 'example-id'}},
    )
