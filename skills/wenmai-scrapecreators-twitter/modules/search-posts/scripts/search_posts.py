#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Twitter standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_posts.py',
        path='/scrapecreators/twitter-search-posts',
        required_fields=['query'],
        sample_params={'query': 'ai agents'},
    )
