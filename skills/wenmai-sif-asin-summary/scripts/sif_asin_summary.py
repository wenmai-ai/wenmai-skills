#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sif_asin_summary.py',
        path='/sif/ops-get-listing-traffic-overview',
        required_fields=['asin'],
        sample_params={'asin': 'B08GHW4TBS', 'country': 'US', 'timePieceType': 'latelyDay', 'timePieceValue': '7'},
    )
