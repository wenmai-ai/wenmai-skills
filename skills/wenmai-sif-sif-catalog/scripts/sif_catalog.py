#!/usr/bin/env python3
"""Call the fixed Wenmai SIF `sif_catalog` standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='sif_catalog.py',
        path='/sif/sif-catalog',
        required_fields=[],
        sample_params={},
    )
