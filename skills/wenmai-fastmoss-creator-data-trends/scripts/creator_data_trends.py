#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `creator_data_trends` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="creator_data_trends.py",
        path="fastmoss/creator-data-trends",
        required_fields=['filter', 'filter.field_type', 'filter.uid'],
        sample_params={'filter': {'field_type': 1, 'uid': 'example-id'}},
    )
