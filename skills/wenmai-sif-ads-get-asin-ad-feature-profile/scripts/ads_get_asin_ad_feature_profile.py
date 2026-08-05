#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_asin_ad_feature_profile` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_asin_ad_feature_profile.py',
        path='/sif/ads-get-asin-ad-feature-profile',
        required_fields=['asin', 'country', 'start_date', 'end_date'],
        sample_params={'asin': 'B08GHW4TBS', 'country': 'US', 'end_date': '2026-04-04', 'start_date': '2026-03-29'},
    )
