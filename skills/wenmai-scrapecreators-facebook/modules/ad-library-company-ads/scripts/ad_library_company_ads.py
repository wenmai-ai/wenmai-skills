#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ad_library_company_ads.py',
        path='/scrapecreators/facebook-ad-library-company-ads',
        required_fields=[],
        sample_params={'companyName': 'Gymshark', 'country': 'US', 'trim': True},
    )
