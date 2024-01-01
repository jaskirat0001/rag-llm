# import os
# import requests
# import json
# from dotenv import load_dotenv
# from urllib.parse import urlencode


# load_dotenv()

# api_key = os.environ.get("Flight_API_KEY", "")
# # Mock fligth API response if base_url is not specified
# base_url = os.environ.get("FLIGHT_BASE_URL", "https://run.mocky.io/v3/c758d798-48aa-42eb-b2d2-8303c2b7542f/request")

# base_params = {
#     "api_key": api_key,
#     "type": "deals",
#     "amazon_domain": "amazon.com"
# }


# def get_url(params):
#     query_parameters = {**base_params, **params}

#     encoded_parameters = urlencode(query_parameters)
#     return f"{base_url}?{encoded_parameters}"


# def send_request(data_dir, params):
#     response = requests.get(get_url(params))

#     if response.status_code == 200:
#         data = response.json()

#         deals_results = data.get('deals_results', [])

#         with open(data_dir + "/rainforest_discounts.jsonl", 'w') as file:
#             for deal in deals_results:
#                 deal['deal_price'] = deal.get('deal_price', {}).get('value', '')
#                 deal['old_price'] = deal.get('list_price', {}).get('value', '')
#                 deal['currency'] = deal.get('list_price', {}).get('currency', '')
#                 doc_object = {"doc": str(deal)}
#                 file.write(json.dumps(doc_object) + '\n')
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
import os
import requests
import json
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

amadeus_api_key = os.environ.get("AMADEUS_API_KEY", "")
base_url = "https://api.amadeus.com/v1/your/amadeus/endpoint"  # Replace with the actual Amadeus API endpoint

base_params = {
    "apikey": amadeus_api_key,
    # Add other Amadeus API parameters as needed
}

def get_url(params):
    query_parameters = {**base_params, **params}
    encoded_parameters = urlencode(query_parameters)
    return f"{base_url}?{encoded_parameters}"

def send_amadeus_request(data_dir, params):
    response = requests.get(get_url(params))

    if response.status_code == 200:
        data = response.json()

        # Handle the Amadeus API response as needed
        # Replace the following lines with the actual response parsing based on the Amadeus API
        # For example:
        # flight_results = data.get('results', [])

        with open(data_dir + "/amadeus_flight_data.jsonl", 'w') as file:
            for result in flight_results:
                doc_object = {"doc": str(result)}
                file.write(json.dumps(doc_object) + '\n')
    else:
        print(f"Failed to fetch Amadeus flight data. Status code: {response.status_code}")

# Example parameters for an Amadeus API request
amadeus_params = {
    "origin": "NYC",
    "destination": "LON",
    # Add other Amadeus API parameters as needed
}

send_amadeus_request("./examples/amadeus", amadeus_params)
