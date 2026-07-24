#!/usr/bin/env python3
"""Call one fixed Wenmai SellerSprite standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='google_trend.py',
        path='/sellersprite/google-trend',
        required_fields=['request', 'request.marketplace'],
        sample_params={'request': {'marketplace': 'US'}},
    )
