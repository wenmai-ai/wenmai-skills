#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='group_posts.py',
        path='/scrapecreators/facebook-group-posts',
        required_fields=[],
        sample_params={'url': 'https://www.facebook.com/groups/python'},
    )
