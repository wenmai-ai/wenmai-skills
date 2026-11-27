#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_hashtag.py',
        path='/scrapecreators/youtube-search-hashtag',
        required_fields=['hashtag'],
        sample_params={'hashtag': 'gymshark', 'type': 'all'},
    )
