#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Reddit standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='subreddit.py',
        path='/scrapecreators/reddit-subreddit',
        required_fields=['subreddit'],
        sample_params={'subreddit': 'AskReddit', 'sort': 'hot'},
    )
