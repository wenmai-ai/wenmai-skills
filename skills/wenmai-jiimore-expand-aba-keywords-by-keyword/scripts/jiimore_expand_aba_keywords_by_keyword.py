#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_expand_aba_keywords_by_keyword.py',
        path='/jiimore/aba-keywords-by-keyword',
        required_fields=['request', 'request.keywords'],
        sample_params={'request': {'keywords': ['neck fan'], 'countryCode': 'US'}},
    )
