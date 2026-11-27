#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='highlight_detail.py',
        path='/scrapecreators/instagram-highlight-detail',
        required_fields=[],
        sample_params={'id': '18125552704906006'},
    )
