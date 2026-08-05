#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_keyword_extends` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_keyword_extends.py',
        path='/sorftime/walmart-keyword-extends',
        required_fields=['keyword'],
        sample_params={'keyword': 'wireless earbuds'},
    )
