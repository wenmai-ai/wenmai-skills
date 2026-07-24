#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_google_trends_scraper.py',
        path='/alpha/google-trends-scraper',
        required_fields=[],
        sample_params={'geo': '', 'category': '', 'maxItems': 0, 'startUrls': [{'url': 'https://trends.google.com/trends/explore?q=web+scraping&geo=US'}], 'timeRange': '', 'isMultiple': False, 'viewedFrom': '', 'searchTerms': ['webscraping'], 'spreadsheetId': '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms', 'maxConcurrency': 3, 'customTimeRange': '2024-01-01 2024-12-31', 'skipDebugScreen': False, 'maxRequestRetries': 3, 'pageLoadTimeoutSecs': 3},
    )
