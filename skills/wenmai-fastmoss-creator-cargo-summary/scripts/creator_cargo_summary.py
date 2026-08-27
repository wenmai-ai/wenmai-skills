#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `creator_cargo_summary` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="creator_cargo_summary.py",
        path="fastmoss/creator-cargo-summary",
        required_fields=['filter', 'filter.uid'],
        sample_params={'filter': {'uid': 'example-id'}},
    )
