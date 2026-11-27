#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_profiles.py',
        path='/scrapecreators/instagram-search-profiles',
        required_fields=['query'],
        sample_params={'query': 'gymshark'},
    )
