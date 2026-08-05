#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_keywords` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_keywords.py',
        path='/sorftime/category-keywords',
        required_fields=['node_id', 'amz_site'],
        sample_params={'node_id': '1055398', 'amz_site': 'US'},
    )
