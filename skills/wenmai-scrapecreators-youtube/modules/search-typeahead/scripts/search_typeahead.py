#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='search_typeahead.py',
        path='/scrapecreators/youtube-search-typeahead',
        required_fields=['query'],
        sample_params={'query': 'gymshark'},
    )
