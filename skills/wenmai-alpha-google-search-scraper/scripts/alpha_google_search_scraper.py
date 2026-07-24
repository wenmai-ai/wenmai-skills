#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_google_search_scraper.py',
        path='/alpha/google-search-scraper',
        required_fields=['queries'],
        sample_params={'queries': 'best wireless earbuds', 'countryCode': 'us', 'languageCode': 'en', 'searchLanguage': 'en', 'maxPagesPerQuery': 1},
    )
