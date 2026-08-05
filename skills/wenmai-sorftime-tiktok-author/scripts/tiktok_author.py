#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `tiktok_author` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='tiktok_author.py',
        path='/sorftime/tiktok-author',
        required_fields=['author_id'],
        sample_params={'author_id': 'xmw_us'},
    )
