#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='profile_reels.py',
        path='/scrapecreators/facebook-profile-reels',
        required_fields=['url'],
        sample_params={'url': 'https://www.facebook.com/gymshark'},
    )
