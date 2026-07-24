#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_xiaohongshu_pro_scraper.py',
        path='/alpha/xiaohongshu-pro-scraper',
        required_fields=[],
        sample_params={'mode': 'search', 'keywords': ['AI'], 'noteType': '不限', 'sortType': 'general', 'timeFilter': '不限', 'fetchComments': False, 'maxItemsPerInput': 3},
    )
