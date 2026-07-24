#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_zalando_scraper.py',
        path='/alpha/zalando-scraper',
        required_fields=['startUrls'],
        sample_params={'maxItems': 3, 'startUrls': [{'url': 'https://www.zalando.at/herren/?q=cap+trucker'}], 'scrapeDetails': False},
    )
