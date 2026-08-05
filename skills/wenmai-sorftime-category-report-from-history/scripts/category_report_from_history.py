#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_report_from_history` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_report_from_history.py',
        path='/sorftime/category-report-from-history',
        required_fields=['start_date', 'end_date', 'node_id', 'amz_site'],
        sample_params={'start_date': '2026-06-01', 'end_date': '2026-06-30', 'node_id': '1055398', 'amz_site': 'US'},
    )
