#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Reddit standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='post_comments.py',
        path='/scrapecreators/reddit-post-comments',
        required_fields=['url'],
        sample_params={'url': 'https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/'},
    )
