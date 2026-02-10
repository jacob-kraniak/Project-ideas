import pandas as pd
import json
from datetime import datetime
from math import radians, cos, sin, asin, sqrt  # For haversine distance

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    return asin(sqrt(a)) * 6371 * 2  # km; >0.8 km ~0.5 miles for non-home

with open('charge_history.json', 'r') as f:
    history = json.load(f)

df = pd.DataFrame(history)
df['start_time'] = pd.to_datetime(df['start_time'])  # Adjust key if different
df['month'] = df['start_time'].dt.to_period('M')

# Filter public
df['is_public'] = df.apply(lambda row: row.get('fast_charger_type') == 'supercharger' or 
                           haversine(row['location']['lat'], row['location']['lon'], home_lat, home_lon) > 0.8, axis=1)
public_df = df[df['is_public']]

monthly_summary = public_df.groupby('month').agg({
    'id': 'count',  # Sessions
    'energy_added_kwh': 'sum',
    'cost': 'sum'
}).rename(columns={'id': 'Sessions'})

md = "# Tesla Public Charging Dashboard\n\n## Monthly Summary\n" + monthly_summary.to_markdown() + "\n\n## Recent Public Sessions\n" + public_df.tail(10).to_markdown()

with open('dashboard.md', 'w') as f:
    f.write(md)
