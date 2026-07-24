#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keepa_product_search.py',
        path='/keepa/keepa-product-search',
        required_fields=['domain', 'term'],
        sample_params={'domain': 1, 'term': 'water bottle', 'page': 0, 'asins-only': 1},
    )
