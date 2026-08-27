#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `creator_rank_top_growth` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="creator_rank_top_growth.py",
        path="fastmoss/creator-rank-top-growth",
        required_fields=['filter.date_type', 'filter.date_value', 'filter.date_info'],
        sample_params={'filter': {'date_type': 1, 'date_value': 'example', 'date_info': {}}},
    )
