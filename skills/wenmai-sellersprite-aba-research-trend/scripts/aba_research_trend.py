#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `aba_research_trend` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='aba_research_trend.py',
        path='/sellersprite/aba-research-trend',
        required_fields=['marketplace', 'keyword'],
        sample_params={'keyword': 'wireless earbuds', 'marketplace': 'US'},
    )
