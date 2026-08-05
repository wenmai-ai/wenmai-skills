#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `keyword_detail` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_detail.py',
        path='/sorftime/keyword-detail',
        required_fields=['keyword', 'keyword_support_site'],
        sample_params={'keyword': 'wireless earbuds', 'keyword_support_site': 'US'},
    )
