#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_asin_ad_window_feature_profile` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_asin_ad_window_feature_profile.py',
        path='/sif/ads-get-asin-ad-window-feature-profile',
        required_fields=['asin', 'country', 'granularity'],
        sample_params={'asin': 'B08GHW4TBS', 'country': 'US', 'granularity': 'week'},
    )
