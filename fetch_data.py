import json
from nsepython import nse_get_fno_lot_size, nse_get_index_list, nse_get_advances_declines, nse_get_index_quote
import os

def fetch_market_data():
    try:
        # Fetching Nifty 50 overview
        # Note: In a production environment, you'd iterate through symbols for more detail
        data = nse_get_index_quote("NIFTY 50")
        
        # Structure the data for your frontend
        market_data = {
            "timestamp": data.get('timestamp', 'N/A'),
            "indexName": "NIFTY 50",
            "lastPrice": data.get('lastPrice'),
            "change": data.get('change'),
            "pChange": data.get('pChange')
        }
        
        with open('data.json', 'w') as f:
            json.dump(market_data, f, indent=4)
        print("Successfully updated data.json")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_market_data()
