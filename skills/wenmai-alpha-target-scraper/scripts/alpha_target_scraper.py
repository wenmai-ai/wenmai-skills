#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_target_scraper.py',
        path='/alpha/target-scraper',
        required_fields=['searchQueries'],
        sample_params={'sort': 'relevance', 'searchQueries': ['laptop'], 'maxSearchPages': 1, 'maxRequestRetries': 3, 'maxProductsPerSearch': 3},
    )
