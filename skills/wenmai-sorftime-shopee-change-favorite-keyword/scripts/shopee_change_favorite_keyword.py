#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_change_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_change_favorite_keyword.py',
        path='/sorftime/shopee-change-favorite-keyword',
        required_fields=['keyword', 'to_dict', 'site'],
        sample_params={'keyword': 'example-keyword', 'to_dict': 'example-folder', 'site': 'TH'},
    )
