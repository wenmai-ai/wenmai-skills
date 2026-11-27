#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='reels_trending.py',
        path='/scrapecreators/instagram-reels-trending',
        required_fields=[],
        sample_params={},
    )
