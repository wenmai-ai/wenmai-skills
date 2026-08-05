#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sellersprite_market_statistics.py',
        path='/sellersprite/market-research-statistics',
        required_fields=['request'],
        enum_fields={'request.marketplace': ['US', 'JP', 'UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'IN']},
        sample_params={'request': {'marketplace': 'US', 'nodeIdPath': '172282:281407', 'topN': 10}},
    )
