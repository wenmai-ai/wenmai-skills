#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_report` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_report.py',
        path='/sorftime/category-report',
        required_fields=['node_id', 'amz_site'],
        sample_params={'node_id': '1055398', 'amz_site': 'US'},
    )
