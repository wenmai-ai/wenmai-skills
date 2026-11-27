#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ad_library_ad_transcript.py',
        path='/scrapecreators/facebook-ad-library-ad-transcript',
        required_fields=[],
        sample_params={'id': '120229348090250398'},
    )
