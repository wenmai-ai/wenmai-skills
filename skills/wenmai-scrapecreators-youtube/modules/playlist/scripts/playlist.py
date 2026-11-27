#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='playlist.py',
        path='/scrapecreators/youtube-playlist',
        required_fields=['playlist_id'],
        sample_params={'playlist_id': 'PLP32wGpgzmIlInfgKVFfCwVsxgGqZNIiS'},
    )
