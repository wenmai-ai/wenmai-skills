#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='community_post.py',
        path='/scrapecreators/youtube-community-post',
        required_fields=['url'],
        sample_params={'url': 'https://www.youtube.com/post/Ugkxvj2KoApYAXoqLWnKVr6zZe5JjeHrQeP8'},
    )
