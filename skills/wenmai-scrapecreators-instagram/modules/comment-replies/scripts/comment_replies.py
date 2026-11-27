#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='comment_replies.py',
        path='/scrapecreators/instagram-comment-replies',
        required_fields=['url', 'comment_id'],
        sample_params={'url': 'https://www.instagram.com/p/Df5MwAKiCVI/', 'comment_id': '18104065796374460'},
    )
