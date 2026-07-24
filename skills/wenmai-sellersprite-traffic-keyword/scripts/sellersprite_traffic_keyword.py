#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sellersprite_traffic_keyword.py',
        path='/sellersprite/traffic-keyword',
        required_fields=['request'],
        sample_params={'request': {'marketplace': 'US', 'asin': 'B08GHW4TBS', 'page': 1, 'size': 50}},
    )
