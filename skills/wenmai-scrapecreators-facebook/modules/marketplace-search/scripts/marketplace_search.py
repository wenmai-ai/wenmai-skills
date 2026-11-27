#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='marketplace_search.py',
        path='/scrapecreators/facebook-marketplace-search',
        required_fields=['lat', 'lng'],
        sample_params={'query': 'gymshark', 'lat': 34.0522, 'lng': -118.2437},
    )
