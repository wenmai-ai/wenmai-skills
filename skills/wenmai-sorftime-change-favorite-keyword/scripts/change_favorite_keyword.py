#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `change_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='change_favorite_keyword.py',
        path='/sorftime/change-favorite-keyword',
        required_fields=['keyword', 'to_dict', 'keyword_support_site'],
        sample_params={'keyword': 'example-keyword', 'to_dict': 'example-folder', 'keyword_support_site': 'US'},
    )
