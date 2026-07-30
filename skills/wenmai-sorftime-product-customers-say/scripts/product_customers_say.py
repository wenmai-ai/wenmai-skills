#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_customers_say` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_customers_say.py',
        path='/sorftime/product-customers-say',
        required_fields=['asin', 'site'],
        sample_params={'asin': 'B0CZPLV566', 'site': 'US'},
    )
