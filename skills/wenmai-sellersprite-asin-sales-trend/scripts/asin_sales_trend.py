#!/usr/bin/env python3
"""Call the fixed Wenmai SellerSprite ASIN sales trend endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name="asin_sales_trend.py",
        path="/sellersprite/asin-sales-trend",
        required_fields=["marketplace", "asin"],
        enum_fields={
            "marketplace": ["US", "JP", "UK", "DE", "FR", "IT", "ES", "CA", "IN"]
        },
        sample_params={"marketplace": "US", "asin": "B08GHW4TBS"},
    )
