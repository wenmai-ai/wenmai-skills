#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_change_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_change_favorite_keyword.py',
        path='/sorftime/walmart-change-favorite-keyword',
        required_fields=['keyword', 'to_dict'],
        sample_params={'keyword': 'example-keyword', 'to_dict': 'example-folder'},
    )
