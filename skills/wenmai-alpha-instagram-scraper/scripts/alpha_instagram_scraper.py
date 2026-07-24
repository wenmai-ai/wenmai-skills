#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_instagram_scraper.py',
        path='/alpha/instagram-scraper',
        required_fields=[],
        sample_params={'search': 'keyboard', 'directUrls': ['https://www.instagram.com/humansofny/'], 'searchType': 'hashtag', 'resultsType': 'posts', 'searchLimit': 3, 'resultsLimit': 3, 'addParentData': False},
    )
