#!/usr/bin/env python3
"""Call one fixed Wenmai SellerSprite standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='review.py',
        path='/sellersprite/review',
        required_fields=['marketplace', 'asin'],
        sample_params={'marketplace': 'US', 'asin': 'B08GHW4TBS'},
    )
