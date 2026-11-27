#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS YouTube standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='video_comment_replies.py',
        path='/scrapecreators/youtube-video-comment-replies',
        required_fields=['continuationToken'],
        sample_params={'continuationToken': 'Eg0SC2RRdzR3OVdnWGNRGAYygwEaUBIa'},
    )
