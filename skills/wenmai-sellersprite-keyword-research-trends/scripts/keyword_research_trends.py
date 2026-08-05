#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `keyword_research_trends` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_research_trends.py',
        path='/sellersprite/keyword-research-trends',
        required_fields=['marketplace', 'keyword'],
        sample_params={'keyword': 'wireless earbuds', 'marketplace': 'US'},
    )
