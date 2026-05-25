# Family Breach Monitor

import requests
import os
from datetime import datetime

HIBP_API_KEY = os.getenv('HIBP_API_KEY')

def check_breaches(email):
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {'user-agent': 'FamilyBreachMonitor', 'hibp-api-key': HIBP_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

# Example usage
if __name__ == '__main__':
    print('Breach monitoring started...')