#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `category_search_from_top_node` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='category_search_from_top_node.py',
        path='/sorftime/category-search-from-top-node',
        required_fields=['top_node', 'amz_site'],
        sample_params={'top_node': 'Home & Kitchen', 'amz_site': 'US'},
    )
