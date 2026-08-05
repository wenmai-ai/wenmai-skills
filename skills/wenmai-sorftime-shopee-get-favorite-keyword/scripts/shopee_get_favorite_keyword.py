#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_get_favorite_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_get_favorite_keyword.py',
        path='/sorftime/shopee-get-favorite-keyword',
        required_fields=['site'],
        sample_params={'site': 'TH'},
    )
