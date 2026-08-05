#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `keyword_research` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='keyword_research.py',
        path='/sellersprite/keyword-research',
        required_fields=['request', 'request.marketplace'],
        sample_params={'request': {'marketplace': 'US'}},
    )
