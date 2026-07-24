#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='amazon_reviews.py',
        path='/carvenmaster/get-asin-reviews',
        required_fields=['asin', 'country'],
        sample_params={'asin': 'B08N5WRWNW', 'country': 'US', 'sort_by': 'recent', 'filter_by_star': 'all_stars'},
    )
