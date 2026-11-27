#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_videos.py',
        path='/scrapecreators/facebook-search-videos',
        required_fields=['query'],
        sample_params={'query': 'gymshark'},
    )
