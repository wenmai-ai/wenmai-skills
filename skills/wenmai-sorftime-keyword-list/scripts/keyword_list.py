#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `keyword_list` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_list.py',
        path='/sorftime/keyword-list',
        required_fields=['keyword_support_site'],
        sample_params={'keyword_support_site': 'US'},
    )
