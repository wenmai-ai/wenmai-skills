#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_lazada_scraper.py',
        path='/alpha/lazada-scraper',
        required_fields=['mode'],
        sample_params={'mode': 'search', 'urls': ['https://www.lazada.sg/catalog/?q=earbuds'], 'sortBy': 'popularity', 'country': 'sg', 'queries': ['laptop'], 'maxPages': 0, 'maxPrice': 3, 'minPrice': 1, 'minRating': 1, 'categoryId': 'keyboard', 'maxListings': 3, 'reviewsOnly': False, 'fetchDetails': False, 'fetchReviews': False, 'freeShippingOnly': False, 'maxNotifyListings': 3, 'maxReviewsPerProduct': 3},
    )
