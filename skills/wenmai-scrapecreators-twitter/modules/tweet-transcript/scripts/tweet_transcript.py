#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Twitter standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tweet_transcript.py',
        path='/scrapecreators/twitter-tweet-transcript',
        required_fields=['url'],
        sample_params={'url': 'https://x.com/TheoVon/status/1916982720317821050'},
    )
