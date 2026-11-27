#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='profile.py',
        path='/scrapecreators/tiktok-profile',
        required_fields=[],
        sample_params={'handle': 'gymshark', 'cache_max_age': '7d'},
    )
