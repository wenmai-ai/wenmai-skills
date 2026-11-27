#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='user_tagged_posts.py',
        path='/scrapecreators/instagram-user-tagged-posts',
        required_fields=['user_id'],
        sample_params={'user_id': '390927249'},
    )
