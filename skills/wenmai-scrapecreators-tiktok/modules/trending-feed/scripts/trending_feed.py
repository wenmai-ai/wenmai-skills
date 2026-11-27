#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='trending_feed.py',
        path='/scrapecreators/tiktok-trending-feed',
        required_fields=['region'],
        sample_params={'region': 'US', 'trim': True},
    )
