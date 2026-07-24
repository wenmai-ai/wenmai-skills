#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_search_keywords_batch.py',
        path='/jiimore/keywords-batch',
        required_fields=['request', 'request.keywords'],
        sample_params={'request': {'keywords': ['neck fan'], 'countryCode': 'US'}},
    )
