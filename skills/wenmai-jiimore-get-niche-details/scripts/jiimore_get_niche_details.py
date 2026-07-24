#!/usr/bin/env python3
"""Call one fixed Wenmai JIIMORE standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='jiimore_get_niche_details.py',
        path='/jiimore/niche-details',
        required_fields=['request', 'request.nicheId'],
        sample_params={'request': {'nicheId': 'sample-niche', 'countryCode': 'US'}},
    )
