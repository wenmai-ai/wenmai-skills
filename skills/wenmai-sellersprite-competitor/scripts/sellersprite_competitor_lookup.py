#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sellersprite_competitor_lookup.py',
        path='/sellersprite/competitor-lookup',
        required_fields=['request'],
        enum_fields={'request.marketplace': ['US', 'JP', 'UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'IN']},
        sample_params={'request': {'marketplace': 'US', 'asins': ['B08GHW4TBS'], 'page': 1, 'size': 50}},
    )
