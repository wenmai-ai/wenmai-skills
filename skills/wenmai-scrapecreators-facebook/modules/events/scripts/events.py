#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='events.py',
        path='/scrapecreators/facebook-events',
        required_fields=['url'],
        sample_params={'url': 'https://www.facebook.com/events/explore/los-angeles-california/112035925469106/', 'time': 'this_week'},
    )
