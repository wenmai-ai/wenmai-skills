#!/usr/bin/env python3
"""Call the fixed Wenmai Sorftime `ali1688_product_search_from_image` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='ali1688_product_search_from_image.py',
        path='/sorftime/ali1688-product-search-from-image',
        required_fields=['image_url'],
        sample_params={'image_url': 'https://cbu01.alicdn.com/img/ibank/O1CN01HrY28j1LS4eMNQV1G_!!3086091297-0-cib.jpg'},
    )
