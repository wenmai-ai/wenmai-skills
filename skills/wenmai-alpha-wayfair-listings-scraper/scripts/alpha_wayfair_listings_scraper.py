#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_wayfair_listings_scraper.py',
        path='/alpha/wayfair-listings-scraper',
        required_fields=['startUrls'],
        sample_params={'startUrls': [{'url': 'https://www.wayfair.com/furniture/sb0/sofas-c413892.html'}], 'maxResults': 3},
    )
