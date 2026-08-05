#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `analyze_traffic_anomaly` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='analyze_traffic_anomaly.py',
        path='/sif/analyze-traffic-anomaly',
        required_fields=['asin'],
        sample_params={'asin': 'B08GHW4TBS'},
    )
