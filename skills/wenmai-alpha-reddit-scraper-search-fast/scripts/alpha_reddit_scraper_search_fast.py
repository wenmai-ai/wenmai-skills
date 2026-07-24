#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_reddit_scraper_search_fast.py',
        path='/alpha/reddit-scraper-search-fast',
        required_fields=[],
        sample_params={'sort': 'relevance', 'queries': ['Cheesecake', 'Swimming Pool'], 'maxPosts': 3, 'timeframe': 'all', 'includeNsfw': False, 'maxComments': 3, 'strictSearch': False, 'subredditSort': 'relevance', 'scrapeComments': False, 'content_analysis': False, 'maximize_coverage': False, 'strictTokenFilter': False, 'subredditKeywords': ['keyboard'], 'sentiment_analysis': False, 'subredditTimeframe': 'all', 'forceSortNewForTimeFilteredRuns': False},
    )
