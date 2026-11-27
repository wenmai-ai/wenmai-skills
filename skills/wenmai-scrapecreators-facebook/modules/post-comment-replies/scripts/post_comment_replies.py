#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='post_comment_replies.py',
        path='/scrapecreators/facebook-post-comment-replies',
        required_fields=['feedback_id', 'expansion_token'],
        sample_params={'feedback_id': 'replace-from-comments', 'expansion_token': 'replace-from-comments'},
    )
