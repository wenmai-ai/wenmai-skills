#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Reddit standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='post_transcript.py',
        path='/scrapecreators/reddit-post-transcript',
        required_fields=['url'],
        sample_params={'url': 'https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/football_nostalgiasa', 'language': 'en'},
    )
