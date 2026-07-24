#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_find_similar_asins.py',
        path='/jiimore/similar-asins',
        required_fields=['request', 'request.asins'],
        sample_params={'request': {'asins': ['B09PCSR9SX'], 'countryCode': 'US'}},
    )
