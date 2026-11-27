#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Instagram standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='audio_reels.py',
        path='/scrapecreators/instagram-audio-reels',
        required_fields=['audio_id'],
        sample_params={'audio_id': '1392969992841787'},
    )
