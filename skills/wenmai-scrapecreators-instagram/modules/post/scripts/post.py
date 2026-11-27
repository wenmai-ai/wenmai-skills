#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='post.py',
        path='/scrapecreators/instagram-post',
        required_fields=['url'],
        sample_params={'url': 'https://www.instagram.com/p/Df5MwAKiCVI/', 'trim': True},
    )
