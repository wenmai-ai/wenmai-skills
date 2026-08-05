#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `competitor_product_keywords` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='competitor_product_keywords.py',
        path='/sorftime/competitor-product-keywords',
        required_fields=['asin', 'keyword_support_site'],
        sample_params={'asin': 'B0CZPLV566', 'keyword_support_site': 'US'},
    )
