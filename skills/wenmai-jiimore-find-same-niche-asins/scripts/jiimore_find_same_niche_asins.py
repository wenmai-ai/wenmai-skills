#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_find_same_niche_asins.py',
        path='/jiimore/same-niche-asins',
        required_fields=['request', 'request.asin'],
        sample_params={'request': {'asin': 'B09PCSR9SX', 'countryCode': 'US'}},
    )
