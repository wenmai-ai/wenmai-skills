#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='reels_search.py',
        path='/scrapecreators/instagram-reels-search',
        required_fields=['query'],
        sample_params={'query': 'gymshark', 'page': 1},
    )
