#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_ad_group_traffic_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_ad_group_traffic_trend.py',
        path='/sif/ads-get-ad-group-traffic-trend',
        required_fields=['asin', 'campaignId', 'adGroupId'],
        sample_params={'asin': 'B08GHW4TBS', 'adGroupId': 'CCL4', 'campaignId': 'SUBD'},
    )
