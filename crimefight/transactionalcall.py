import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def create_transactional_call(lead_id, transaction_vars):
    api_url = 'https://api.callchimp.ai/v1/calls'
    api_key =os.getenv("API_KEY")
    
    payload = {
        "lead": lead_id,
        "transaction_vars": transaction_vars
    }

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'x-api-key': api_key
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for bad response codes
        print("API Response:")
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating transactional call: {e}")
        return None




def initcall(crime_type, crime_description):
    lead_id = 839686
    
    transaction_vars = {
        "casetype": crime_type,
        "crimedescription": crime_description
    }
    # Call the function to create the transactional call
    create_transactional_call(lead_id, transaction_vars)
   
