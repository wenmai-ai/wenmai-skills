#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='profile_videos.py',
        path='/scrapecreators/tiktok-profile-videos',
        required_fields=['handle'],
        sample_params={'handle': 'gymshark', 'trim': True},
    )
