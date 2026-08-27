#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `video_detail_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="video_detail_analysis.py",
        path="fastmoss/video-detail-analysis",
        required_fields=['filter', 'filter.video_id'],
        sample_params={'filter': {'video_id': 'example-id'}},
    )
