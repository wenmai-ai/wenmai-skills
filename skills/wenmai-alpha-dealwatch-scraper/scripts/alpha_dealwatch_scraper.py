#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_dealwatch_scraper.py',
        path='/alpha/dealwatch-scraper',
        required_fields=['zip_codes'],
        sample_params={'store': 'homedepot.com', 'keywords': ['screwdriver', 'drill', 'generator', 'grill'], 'zip_codes': ['28546']},
    )
