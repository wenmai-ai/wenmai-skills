#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='live_info.py',
        path='/scrapecreators/tiktok-live-info',
        required_fields=['room_id', 'user_id'],
        sample_params={'room_id': '7442820520199981856', 'user_id': '6536068161471517696'},
    )
