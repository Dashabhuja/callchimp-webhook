from flask import Flask, request, jsonify
import requests
from azure import analyze_script_severity, casecreater, describer
from initcall import startcall
from updatescript import scriptupdater
from transactionalcall import initcall
from flask_cors import CORS
from twilio.rest import Client
import logging
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow CORS from all origins

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_twilio_message(message_body, to_phone_number):
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
@app.route('/', methods=['GET'])
def home():
    return "You are at callchimp webhook endpoint."


@app.route('/analyse', methods=['POST'])
def analysis():
    # Parse the incoming JSON data
    data = request.json
    script = str(data['description'])  # Hold the description in the script variable
    print("Script for analysis:", script)
    analysis_result = analyze_script_severity(script)
    
    print("Analysis result:", analysis_result['choices'][0]['message']['content'])
    if "severity:true" in analysis_result['choices'][0]['message']['content']:
        print("Severity detected.")
        scriptcreation(data)
    # Your existing analysis logic here
    return jsonify({"status": "analysis done", "analysis_result": analysis_result['choices'][0]['message']['content']})



def scriptcreation(data):
    # Parse the incoming JSON data
    
    script = str(data) 
    crime_type = str(data['type']) # Hold the description in the script variable

    print("Describer Recived :", data)
    script_json = describer(script)
    
    print("Analysis result:", script_json)
    New_script = script_json['choices'][0]['message']['content']
    # Updtating your new generated script
    
    New_script =scriptupdater(str(crime_type),str(New_script))
    # Start a call with by sending transectional_vars 
    startcall()

    
    
    # Your existing analysis logic here
    return jsonify({"status": "analysis done", "analysis_result": "call Initiated"})



def process_json_response(response):
    """
    Process the JSON response to check for a specific sentence in the bot responses.

    Args:
        response (dict): The JSON response from the client.

    Returns:
        str: A message indicating whether the specific sentence was found.
    """
    specific_sentence_fragment = "A link with the detailed description of the case has been sent to your mobile"
    data = response.get('data', {})
    for entry in data.get('transcript', []):
        if specific_sentence_fragment in entry.get('bot', ''):
            logging.info("Specific sentence fragment found in the bot response. Performing the desired task...")
            response = casecreater(data)
            result = response['choices'][0]['message']['content']
            logging.info(result)
            send_twilio_message(result, RECIPIENT_PHONE_NUMBER)
            return "Specific sentence fragment found and task performed."
    return "Specific sentence fragment not found in the bot responses."






@app.route('/webhook-endpoint', methods=['POST'])
def webhook_received():
    # Parse the incoming JSON data
    data = request.json
    print("Received data:", data)
    result = process_json_response(data)
    print(result)
    # Example: Process the data and decide on the response
    # This is where you'd add your logic based on the webhook data received
    # For demonstration, let's assume we're sending a simple text response
    response_data = {
        "message": "Your response was received and processed!"
    }
    
    # Example: Send a response back to a hypothetical endpoint
    # This could be another API call to send a response back to the user or another service
    response_url = "https://example.com/respond"
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(response_url, json=response_data, headers=headers)
        if response.status_code == 200:
            print("Response successfully sent.")
        else:
            print("Failed to send response.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Acknowledge the webhook
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
