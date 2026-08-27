#!/usr/bin/env python3
"""Call the fixed Wenmai FastMoss `product_rank_new_listed` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="product_rank_new_listed.py",
        path="fastmoss/product-rank-new-listed",
        required_fields=['filter.listing_end_date', 'filter.listing_start_date', 'filter.date_info'],
        sample_params={'filter': {'listing_end_date': 'example', 'listing_start_date': 'example', 'date_info': {}}},
    )
