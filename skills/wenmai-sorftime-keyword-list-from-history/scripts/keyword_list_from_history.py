#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `keyword_list_from_history` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_list_from_history.py',
        path='/sorftime/keyword-list-from-history',
        required_fields=['date', 'keyword_support_site'],
        sample_params={'date': '2026-06-30', 'keyword_support_site': 'US'},
    )
