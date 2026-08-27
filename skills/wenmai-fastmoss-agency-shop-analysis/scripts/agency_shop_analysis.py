#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `agency_shop_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="agency_shop_analysis.py",
        path="fastmoss/agency-shop-analysis",
        required_fields=['filter', 'filter.agency_id'],
        sample_params={'filter': {'agency_id': 'example-id'}},
    )
