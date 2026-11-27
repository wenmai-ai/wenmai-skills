#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_keyword.py',
        path='/scrapecreators/tiktok-search-keyword',
        required_fields=['query'],
        sample_params={'query': 'amazon finds', 'region': 'US', 'trim': True},
    )
