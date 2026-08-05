#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite `bsr_prediction` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='bsr_prediction.py',
        path='/sellersprite/bsr-prediction',
        required_fields=['marketplace', 'bsr', 'categoryId'],
        sample_params={'bsr': 1, 'categoryId': '11260432011', 'marketplace': 'US'},
    )
