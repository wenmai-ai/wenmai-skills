#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Twitter standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='community.py',
        path='/scrapecreators/twitter-community',
        required_fields=['url'],
        sample_params={'url': 'https://x.com/i/communities/1926186499399139650'},
    )
