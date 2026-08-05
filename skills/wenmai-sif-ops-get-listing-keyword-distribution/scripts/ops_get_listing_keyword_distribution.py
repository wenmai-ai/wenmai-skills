#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ops_get_listing_keyword_distribution` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ops_get_listing_keyword_distribution.py',
        path='/sif/ops-get-listing-keyword-distribution',
        required_fields=['asin'],
        sample_params={'asin': 'B08GHW4TBS'},
    )
