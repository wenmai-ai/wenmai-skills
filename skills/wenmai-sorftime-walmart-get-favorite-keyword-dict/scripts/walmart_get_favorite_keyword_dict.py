#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_get_favorite_keyword_dict` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_get_favorite_keyword_dict.py',
        path='/sorftime/walmart-get-favorite-keyword-dict',
        required_fields=[],
        sample_params={},
    )
