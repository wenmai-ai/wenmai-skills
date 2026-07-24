#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_youtube_comments_scraper.py',
        path='/alpha/youtube-comments-scraper',
        required_fields=['startUrls'],
        sample_params={'startUrls': [{'url': 'https://www.youtube.com/watch?v=xObhZ0Ga7EQ'}], 'maxComments': 3, 'sortCommentsBy': 'NEWEST_FIRST', 'oldestCommentDate': '2026-03-01'},
    )
