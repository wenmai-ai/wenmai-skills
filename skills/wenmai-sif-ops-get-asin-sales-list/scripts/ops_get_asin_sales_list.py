#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `ops_get_asin_sales_list` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ops_get_asin_sales_list.py',
        path='/sif/ops-get-asin-sales-list',
        required_fields=['asins'],
        sample_params={'asins': ['B08GHW4TBS']},
    )
