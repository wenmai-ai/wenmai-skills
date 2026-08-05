#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ads_get_campaign_contribution_breakdown` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ads_get_campaign_contribution_breakdown.py',
        path='/sif/ads-get-campaign-contribution-breakdown',
        required_fields=['asin', 'campaignId', 'start_date', 'end_date', 'breakdown_by'],
        sample_params={'asin': 'B08GHW4TBS', 'end_date': '2026-04-04', 'campaignId': 'SUBD', 'start_date': '2026-03-29', 'breakdown_by': 'keyword'},
    )
