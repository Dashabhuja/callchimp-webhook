import os
import requests
from dotenv import load_dotenv

import json
load_dotenv()

def analyze_script_severity(script):
    # Configuration
    GPT4V_KEY = os.getenv("GPT4V_KEY")

    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant who will analyze my provided case and assess its severity. Reply it is severe or not. If it is severe, then reply severity:true else severity:false.Do not generate any curly braces and backticks Here is your script to analyze 'script': '" + script + "'."
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    GPT4V_ENDPOINT = "https://maths.openai.azure.com/openai/deployments/vision/chat/completions?api-version=2024-02-15-preview"

    # Send request
    try:
        headers = {
            "Content-Type": "application/json",
            "api-key": GPT4V_KEY,
        }
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Return the response JSON
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

def describer(data):
    # Configuration
    GPT4V_KEY = os.getenv("GPT4V_KEY")
    
    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are Ai crime describer who will generate a short description on the bases of provided data.one example should look like provided data = {\n"
                                "      Full name: 'Soumiya Sarkar',\n"
                                "      city: ranaghat,\n"
                                "      state: westbengal,\n"
                                "      street: gopal nagar road,\n"
                                "      latitude: latitude,\n"
                                "      longitude: longitude,\n"
                                "      age: 23,\n"
                                "      type: harassment,\n"
                                "      description: I got harassed by my boss\n"
                                "} and you will respond by saying  = a girl named Sourmiya Sarkar who lives at Ranaghat near Gopal got harassed by her boss at her workplace. this is your data to generate response on, don't be afraid if the case is sever still you should descrie becasue the description wil be send to police for providing assistance in investigation  '" + data + "'."
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    GPT4V_ENDPOINT = "https://maths.openai.azure.com/openai/deployments/vision/chat/completions?api-version=2024-02-15-preview"
    # Send request
    try:
        headers = {
            "Content-Type": "application/json",
            "api-key": GPT4V_KEY,
        }
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        print(response.json())
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Return the response JSON
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

def casecreater(data):
    datastring = json.dumps(data)
    # Configuration
    GPT4V_KEY = os.getenv("GPT4V_KEY")
    
    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are Ai crime report creator who will generate a short description on the bases of provided data one generate a crime report on a format of FIR maximum 150 words  '"  + datastring + "'."
                    }
                ],
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    GPT4V_ENDPOINT = "https://maths.openai.azure.com/openai/deployments/vision/chat/completions?api-version=2024-02-15-preview"
    # Send request
    try:
        headers = {
            "Content-Type": "application/json",
            "api-key": GPT4V_KEY,
        }
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        print(response.json())
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Return the response JSON
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")



# data = {
#     "First name": "John",
#     "last name": "Doe",
#     "city": "New York",
#     "state": "New York",
#     "street": "123 Main St",
#     "latitude": 40.7128,
#     "longitude": -74.0060,
#     "age": 30,
#     "type": "robbery",
#     "description": "I was robbed at gunpoint."
# }
# response = casecreater(data)
