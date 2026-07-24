#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_walmart_reviews_scraper.py',
        path='/alpha/walmart-reviews-scraper',
        required_fields=[],
        sample_params={'startUrls': [{'url': 'https://walmart.com/search?q=tshirt'}], 'reviewsSortType': 'relevancy', 'scrapeUntilDate': 'keyboard', 'maxReviewsPerProduct': 3, 'maxProductsPerStartUrl': 3},
    )
