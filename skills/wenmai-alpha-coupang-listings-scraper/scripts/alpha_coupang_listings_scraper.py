#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_coupang_listings_scraper.py',
        path='/alpha/coupang-listings-scraper',
        required_fields=[],
        sample_params={'maxResults': 3, 'searchTerms': ['laptop']},
    )
