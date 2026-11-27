#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ad_library_search_companies.py',
        path='/scrapecreators/facebook-ad-library-search-companies',
        required_fields=['query'],
        sample_params={'query': 'gymshark'},
    )
