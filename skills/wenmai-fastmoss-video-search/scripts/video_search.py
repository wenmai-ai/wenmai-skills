#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `video_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="video_search.py",
        path="fastmoss/video-search",
        required_fields=['filter.create_time_range'],
        sample_params={'filter': {'create_time_range': {}}},
    )
