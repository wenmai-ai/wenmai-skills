#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_facebook_ads_scraper.py',
        path='/alpha/facebook-ads-scraper',
        required_fields=['startUrls'],
        sample_params={'sorting': 'relevancy_monthly_grouped', 'onlyTotal': False, 'startUrls': [{'url': 'https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&search_type=keyword_unordered&q=nike'}], 'activeStatus': 'active', 'resultsLimit': 5},
    )
