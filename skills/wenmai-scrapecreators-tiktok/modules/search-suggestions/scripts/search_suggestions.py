#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_suggestions.py',
        path='/scrapecreators/tiktok-search-suggestions',
        required_fields=['query'],
        sample_params={'query': 'amazon'},
    )
