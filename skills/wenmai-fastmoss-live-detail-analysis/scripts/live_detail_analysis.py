#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `live_detail_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="live_detail_analysis.py",
        path="fastmoss/live-detail-analysis",
        required_fields=['filter', 'filter.room_id'],
        sample_params={'filter': {'room_id': 'example-id'}},
    )
