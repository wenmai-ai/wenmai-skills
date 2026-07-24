#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_noon_com_scraper.py',
        path='/alpha/noon-com-scraper',
        required_fields=[],
        sample_params={'maxPages': 3, 'startUrl': 'https://www.noon.com/uae-en/fashion/men-31225/crazy-price-drops-ae-FA_03/', 'maxProducts': 3},
    )
