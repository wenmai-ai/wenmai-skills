#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='user_embed.py',
        path='/scrapecreators/instagram-user-embed',
        required_fields=['handle'],
        sample_params={'handle': 'gymshark'},
    )
