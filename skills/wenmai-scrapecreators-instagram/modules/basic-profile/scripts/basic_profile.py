#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='basic_profile.py',
        path='/scrapecreators/instagram-basic-profile',
        required_fields=[],
        sample_params={'userId': '390927249'},
    )
