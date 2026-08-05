#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `walmart_keyword_list` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='walmart_keyword_list.py',
        path='/sorftime/walmart-keyword-list',
        required_fields=['rank_min', 'rank_max'],
        sample_params={'rank_min': 1, 'rank_max': 100},
    )
