#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='video_comment_replies.py',
        path='/scrapecreators/tiktok-video-comment-replies',
        required_fields=['comment_id', 'url'],
        sample_params={'url': 'https://www.tiktok.com/@karissa.brighton/video/7702948337007234335', 'comment_id': '7703257909974549279'},
    )
