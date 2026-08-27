#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `creator_profile_overview` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="creator_profile_overview.py",
        path="fastmoss/creator-profile-overview",
        required_fields=['filter', 'filter.uid'],
        sample_params={'filter': {'uid': 'example-id'}},
    )
