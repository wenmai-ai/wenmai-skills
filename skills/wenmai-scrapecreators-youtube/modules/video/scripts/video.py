#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='video.py',
        path='/scrapecreators/youtube-video',
        required_fields=['url'],
        sample_params={'url': 'https://www.youtube.com/watch?v=Y2Ah_DFr8cw'},
    )
