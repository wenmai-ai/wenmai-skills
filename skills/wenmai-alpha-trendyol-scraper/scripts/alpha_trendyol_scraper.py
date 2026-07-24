#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_trendyol_scraper.py',
        path='/alpha/trendyol-scraper',
        required_fields=['mode'],
        sample_params={'mode': 'url', 'urls': ['https://www.trendyol.com/apple/iphone-15-128-gb-siyah-p-762254032'], 'maxPages': 1},
    )
