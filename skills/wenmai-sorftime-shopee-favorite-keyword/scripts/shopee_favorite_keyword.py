#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_favorite_keyword.py',
        path='/sorftime/shopee-favorite-keyword',
        required_fields=['keyword', 'site'],
        sample_params={'keyword': 'example-keyword', 'site': 'TH'},
    )
