#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_ad_group_keyword_breakdown` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_ad_group_keyword_breakdown.py',
        path='/sif/ads-get-ad-group-keyword-breakdown',
        required_fields=['asin', 'campaignId', 'adGroupId', 'date'],
        sample_params={'asin': 'B08GHW4TBS', 'date': '2026-03-29', 'adGroupId': 'CCL4', 'campaignId': 'SUBD'},
    )
