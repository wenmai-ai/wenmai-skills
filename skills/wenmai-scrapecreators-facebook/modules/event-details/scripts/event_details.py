#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='event_details.py',
        path='/scrapecreators/facebook-event-details',
        required_fields=[],
        sample_params={'url': 'https://www.facebook.com/events/2255360061870188'},
    )
