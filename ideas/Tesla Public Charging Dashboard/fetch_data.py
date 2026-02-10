import requests
from dotenv import load_dotenv, find_dotenv, set_key
import os
import json
import pdfplumber  # For cost extraction

load_dotenv()

refresh_token = os.getenv('TESLA_REFRESH_TOKEN')
home_lat = float(os.getenv('HOME_LAT', 40.795))  # Ronkonkoma approx
home_lon = float(os.getenv('HOME_LON', -73.131))

# Refresh access token
data = {
    "grant_type": "refresh_token",
    "client_id": "ownerapi",
    "refresh_token": refresh_token,
    "scope": "openid email offline_access"
}
response = requests.post("https://auth.tesla.com/oauth2/v3/token", json=data)
if response.status_code != 200:
    raise Exception("Refresh failed")
tokens = response.json()
access_token = tokens['access_token']
new_refresh = tokens['refresh_token']

# Update .env with new refresh (for local; Actions needs manual update)
dotenv_path = find_dotenv()
set_key(dotenv_path, 'TESLA_REFRESH_TOKEN', new_refresh)

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Get vehicles
vehicles = requests.get("https://owner-api.teslamotors.com/api/1/vehicles", headers=headers).json()['response']
vehicle_id = vehicles[0]['id']  # Assume one vehicle
vin = vehicles[0]['vin']

# Fetch charging history (paginate)
page = 1
history = []
while True:
    url = "https://owner-api.teslamotors.com/api/1/dx/charging/history"
    params = {"page": page, "size": 50}  # Adjust if API requires dates or other params
    resp = requests.get(url, headers=headers, params=params).json()
    sessions = resp.get('charging_history', [])  # Assumed key
    if not sessions:
        break
    history.extend(sessions)
    page += 1

# Extract costs from invoices
for session in history:
    if 'invoices' in session and session['invoices']:
        invoice = session['invoices'][0]
        invoice_url = f"https://owner-api.teslamotors.com/api/1/dx/charging/invoice/{invoice['contentId']}"
        pdf_resp = requests.get(invoice_url, headers=headers)
        with open('temp.pdf', 'wb') as f:
            f.write(pdf_resp.content)
        with pdfplumber.open('temp.pdf') as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages)
            # Parse for cost (customize based on PDF format, e.g., look for "Total: $XX.XX")
            cost_line = [line for line in text.splitlines() if 'Total' in line]
            session['cost'] = float(cost_line[0].split('$')[1]) if cost_line else 0.0
        os.remove('temp.pdf')
    else:
        session['cost'] = 0.0  # Home/public non-Supercharger

with open('charge_history.json', 'w') as f:
    json.dump(history, f)
