#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='video_comments.py',
        path='/scrapecreators/tiktok-video-comments',
        required_fields=['url'],
        sample_params={'url': 'https://www.tiktok.com/@karissa.brighton/video/7702948337007234335'},
    )
