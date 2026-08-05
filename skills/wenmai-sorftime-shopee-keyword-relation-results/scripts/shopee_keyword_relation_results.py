#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `shopee_keyword_relation_results` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='shopee_keyword_relation_results.py',
        path='/sorftime/shopee-keyword-relation-results',
        required_fields=['site'],
        sample_params={'site': 'TH'},
    )
