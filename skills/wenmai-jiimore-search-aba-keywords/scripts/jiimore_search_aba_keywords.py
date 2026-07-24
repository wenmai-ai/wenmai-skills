#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_search_aba_keywords.py',
        path='/jiimore/aba-keywords',
        required_fields=['request', 'request.asins'],
        sample_params={'request': {'asins': ['B09PCSR9SX'], 'countryCode': 'US'}},
    )
