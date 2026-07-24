#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_tweet_scraper.py',
        path='/alpha/tweet-scraper',
        required_fields=[],
        sample_params={'sort': 'Latest', 'maxItems': 3, 'onlyImage': False, 'onlyQuote': False, 'onlyVideo': False, 'startUrls': ['https://twitter.com/apify', 'https://twitter.com/search?q=apify%20&src=typed_query', 'https://twitter.com/i/lists/78783491', 'https://twitter.com/elonmusk/with_replies'], 'searchTerms': ['web scraping', 'scraping from:apify'], 'tweetLanguage': 'en', 'minimumReplies': 1, 'twitterHandles': ['elonmusk', 'taylorswift13'], 'minimumRetweets': 1, 'onlyTwitterBlue': False, 'minimumFavorites': 1, 'customMapFunction': '(object) => { return {...object} }', 'onlyVerifiedUsers': False, 'includeSearchTerms': False},
    )
