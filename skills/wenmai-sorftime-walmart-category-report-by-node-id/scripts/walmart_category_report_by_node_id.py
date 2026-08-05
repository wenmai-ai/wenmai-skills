#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_category_report_by_node_id` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_category_report_by_node_id.py',
        path='/sorftime/walmart-category-report-by-node-id',
        required_fields=['node_id'],
        sample_params={'node_id': '1055398'},
    )
