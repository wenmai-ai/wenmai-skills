#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_tiktok_scraper.py',
        path='/alpha/tiktok-scraper',
        required_fields=[],
        sample_params={'searchQueries': ['keyboard'], 'searchSection': '/video', 'resultsPerPage': 10},
    )
