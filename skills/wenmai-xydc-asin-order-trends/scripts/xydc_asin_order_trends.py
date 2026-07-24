#!/usr/bin/env python3
"""Call one fixed Wenmai XYDC standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='xydc_asin_order_trends.py',
        path='/xydc/get-asin-order-trends',
        required_fields=['asin', 'country', 'end_month', 'start_month'],
        sample_params={'asin': 'B09PCSR9SX', 'country': 'US', 'start_month': '2026-05', 'end_month': '2026-06'},
    )
