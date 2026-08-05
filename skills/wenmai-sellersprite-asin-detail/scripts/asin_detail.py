#!/usr/bin/env python3
"""Call one fixed Wenmai SellerSprite standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='asin_detail.py',
        path='/sellersprite/asin-detail',
        required_fields=['marketplace', 'asin'],
        enum_fields={'marketplace': ['US', 'JP', 'UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'IN', 'MX', 'BR', 'AU', 'AE']},
        sample_params={'marketplace': 'US', 'asin': 'B08GHW4TBS'},
    )
