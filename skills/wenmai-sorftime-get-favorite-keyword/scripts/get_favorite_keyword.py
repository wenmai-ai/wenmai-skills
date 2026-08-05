#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `get_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='get_favorite_keyword.py',
        path='/sorftime/get-favorite-keyword',
        required_fields=['keyword_support_site'],
        sample_params={'keyword_support_site': 'US'},
    )
