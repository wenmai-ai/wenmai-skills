#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `live_search` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="live_search.py",
        path="fastmoss/live-search",
        required_fields=['filter.start_time'],
        sample_params={'filter': {'start_time': {}}},
    )
