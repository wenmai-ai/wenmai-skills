#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='song.py',
        path='/scrapecreators/tiktok-song',
        required_fields=['clipId'],
        sample_params={'clipId': '7694359127636265750'},
    )
