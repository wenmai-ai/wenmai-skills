#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_rakuten_japan_scraper.py',
        path='/alpha/rakuten-japan-scraper',
        required_fields=[],
        sample_params={'genreId': 'keyboard', 'maxItems': 3, 'maxPrice': 3, 'minPrice': 1, 'startUrl': 'https://www.amazon.com/s?k=keyboard', 'sortOrder': 'standard', 'searchKeyword': 'laptop', 'maxConcurrency': 3},
    )
