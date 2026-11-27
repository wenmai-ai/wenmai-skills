#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Twitter standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tweet.py',
        path='/scrapecreators/twitter-tweet',
        required_fields=['url'],
        sample_params={'url': 'https://x.com/levelsio/status/1834021269559501236'},
    )
