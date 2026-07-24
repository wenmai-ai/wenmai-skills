#!/usr/bin/env python3
"""Call one fixed Wenmai Alpha standard API endpoint."""

from _wenmai_api import run_api


if __name__ == "__main__":
    run_api(
        script_name='alpha_bol_com_scraper.py',
        path='/alpha/bol-com-scraper',
        required_fields=[],
        sample_params={'q': 'keyboard', 'url': 'https://www.amazon.com/s?k=keyboard', 'mode': 'search', 'urls': ['https://www.amazon.com/s?k=keyboard'], 'query': 'keyboard', 'sortBy': 'relevance', 'country': 'be', 'keyword': 'keyboard', 'category': 'keyboard', 'llmModel': 'keyboard', 'maxItems': 3, 'watchMode': False, 'maxResults': 3, 'productUrl': 'https://www.amazon.com/s?k=keyboard', 'searchTerm': 'keyboard', 'bolClientId': 'keyboard', 'llmProvider': 'openrouter', 'maxProducts': 3, 'productUrls': ['https://www.amazon.com/s?k=keyboard'], 'searchQuery': 'PlayStation 5', 'fetchDetails': False, 'googleApiKey': 'keyboard', 'openaiApiKey': 'keyboard', 'ollamaBaseUrl': 'http://localhost:11434', 'includeDetails': False, 'anthropicApiKey': 'keyboard', 'bolClientSecret': 'keyboard', 'enableAiAnalysis': False, 'openrouterApiKey': 'keyboard'},
    )
