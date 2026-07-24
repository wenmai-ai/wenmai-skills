#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_etsy_scraper.py',
        path='/alpha/etsy-scraper',
        required_fields=['searchQuery'],
        sample_params={'sort': 'most_relevant', 'locale': 'en-US', 'onSale': False, 'category': 'jewelry-and-accessories', 'currency': 'USD', 'maxItems': 3, 'maxPrice': 3, 'minPrice': 10, 'searchQuery': 'handmade necklace', 'freeShipping': False, 'excludeKeywords': ['digital', 'download'], 'includeKeywords': ['handmade'], 'excludeDigitalDownloads': False},
    )
