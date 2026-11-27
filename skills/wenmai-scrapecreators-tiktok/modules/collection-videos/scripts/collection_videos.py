#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS TikTok standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='collection_videos.py',
        path='/scrapecreators/tiktok-collection-videos',
        required_fields=['url'],
        sample_params={'url': 'https://www.tiktok.com/@kibblemaster808/collection/Want-to-go-7665668414573546258'},
    )
