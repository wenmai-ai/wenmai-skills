#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `market_category_analysis` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="market_category_analysis.py",
        path="fastmoss/market-category-analysis",
        required_fields=['analysis_type', 'filter'],
        sample_params={'analysis_type': 1, 'filter': {}},
    )
