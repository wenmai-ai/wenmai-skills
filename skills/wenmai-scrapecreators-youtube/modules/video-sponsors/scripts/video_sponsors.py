#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='video_sponsors.py',
        path='/scrapecreators/youtube-video-sponsors',
        required_fields=['url'],
        sample_params={'url': 'https://www.youtube.com/watch?v=AVO0ifle-OU', 'language': 'en'},
    )
