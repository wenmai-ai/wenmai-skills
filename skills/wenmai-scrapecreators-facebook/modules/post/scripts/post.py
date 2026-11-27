#!/usr/bin/env python3
"""Call one fixed Wenmai SCRAPECREATORS Facebook standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='post.py',
        path='/scrapecreators/facebook-post',
        required_fields=['url'],
        sample_params={'url': 'https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l'},
    )
