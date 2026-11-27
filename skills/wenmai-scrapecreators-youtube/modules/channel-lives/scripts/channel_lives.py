#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='channel_lives.py',
        path='/scrapecreators/youtube-channel-lives',
        required_fields=[],
        sample_params={'handle': 'gymshark'},
    )
