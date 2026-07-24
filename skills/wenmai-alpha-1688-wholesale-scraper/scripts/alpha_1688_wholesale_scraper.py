#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_1688_wholesale_scraper.py',
        path='/alpha/1688-wholesale-scraper',
        required_fields=[],
        sample_params={'sortBy': 'relevance', 'keywords': ['phone case'], 'maxResults': 10},
    )
