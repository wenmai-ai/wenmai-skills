#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_mercadolibre_scraper.py',
        path='/alpha/mercadolibre-scraper',
        required_fields=[],
        sample_params={'mode': 'reviews', 'country': 'MX', 'maxItems': 3, 'sellerUrls': ['https://www.mercadolibre.com.mx/tienda/phone-depot'], 'productUrls': ['https://www.mercadolibre.com.mx/apple-iphone-15-256-gb-negro/p/MLM27172669'], 'reviewOrder': 'relevance', 'searchQuery': 'iphone', 'reviewRating': 'all', 'includeReviews': True, 'maxConcurrency': 3, 'includeQuestions': True, 'includeVariations': True, 'maxItemsPerSeller': 0, 'includeFeaturedItems': False, 'includeSellerProfile': True},
    )
