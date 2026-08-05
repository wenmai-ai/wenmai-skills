#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `aba_research_monthly` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='aba_research_monthly.py',
        path='/sellersprite/aba-research-monthly',
        required_fields=['request', 'request.marketplace'],
        sample_params={'request': {'marketplace': 'US'}},
    )
