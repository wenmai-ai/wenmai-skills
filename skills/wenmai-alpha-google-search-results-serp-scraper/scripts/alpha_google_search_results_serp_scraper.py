#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_google_search_results_serp_scraper.py',
        path='/alpha/google-search-results-serp-scraper',
        required_fields=['keyword'],
        sample_params={'cr': 'countryAF', 'gl': 'AF', 'hl': 'af', 'lr': 'lang_af', 'tbs': 'keyboard', 'page': 10, 'limit': 'all', 'start': 1, 'country': 'AF', 'keyword': 'nike', 'include_merged': True},
    )
