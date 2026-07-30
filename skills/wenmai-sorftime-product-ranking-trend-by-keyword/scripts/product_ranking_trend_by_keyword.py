#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `product_ranking_trend_by_keyword` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='product_ranking_trend_by_keyword.py',
        path='/sorftime/product-ranking-trend-by-keyword',
        required_fields=['asin', 'keyword', 'amz_site'],
        sample_params={'asin': 'B0CZPLV566', 'keyword': 'wireless earbuds', 'amz_site': 'US'},
    )
