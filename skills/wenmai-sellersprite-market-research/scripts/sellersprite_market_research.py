#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sellersprite_market_research.py',
        path='/sellersprite/market-research',
        required_fields=['request'],
        sample_params={'request': {'marketplace': 'US', 'nodeIdPath': '172282:281407', 'page': 1, 'size': 50}},
    )
