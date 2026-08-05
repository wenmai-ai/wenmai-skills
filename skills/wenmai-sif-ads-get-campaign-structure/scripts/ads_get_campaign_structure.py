#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_campaign_structure` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_campaign_structure.py',
        path='/sif/ads-get-campaign-structure',
        required_fields=['asin', 'campaignId'],
        sample_params={'asin': 'B08GHW4TBS', 'campaignId': 'SUBD'},
    )
