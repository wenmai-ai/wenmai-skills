#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_find_asins_by_keyword.py',
        path='/jiimore/asins-by-keyword',
        required_fields=['request', 'request.keyword'],
        sample_params={'request': {'keyword': 'neck fan', 'countryCode': 'US'}},
    )
