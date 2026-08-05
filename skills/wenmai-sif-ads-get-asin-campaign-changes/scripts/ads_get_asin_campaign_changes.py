#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_asin_campaign_changes` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_asin_campaign_changes.py',
        path='/sif/ads-get-asin-campaign-changes',
        required_fields=['asin', 'country'],
        sample_params={'asin': 'B08GHW4TBS', 'country': 'US'},
    )
