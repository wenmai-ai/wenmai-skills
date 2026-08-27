#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `market_category_ranking` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="market_category_ranking.py",
        path="fastmoss/market-category-ranking",
        required_fields=[],
        sample_params={},
    )
