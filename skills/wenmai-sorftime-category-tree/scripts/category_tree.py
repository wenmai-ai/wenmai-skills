#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_tree` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_tree.py',
        path='/sorftime/category-tree',
        required_fields=['amz_site'],
        sample_params={'amz_site': 'US'},
    )
