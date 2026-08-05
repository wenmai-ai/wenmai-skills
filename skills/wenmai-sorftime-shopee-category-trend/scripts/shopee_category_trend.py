#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_category_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_category_trend.py',
        path='/sorftime/shopee-category-trend',
        required_fields=['site'],
        sample_params={'site': 'TH'},
    )
