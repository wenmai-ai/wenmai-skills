#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keepa_product_history.py',
        path='/keepa/get-keepa-product-history',
        required_fields=['asin', 'domain'],
        sample_params={'domain': 1, 'asin': 'B08GHW4TBS', 'stats': 90, 'history': True, 'rating': True},
    )
