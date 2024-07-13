import os
from dotenv import load_dotenv
from pprint import pprint
import callchimp
from callchimp.api import ScriptsApi
from callchimp.rest import ApiException

load_dotenv()

def scriptupdater(crime_type, script):
    """
    Update a Callchimp script.

    Args:
        crime_type (str): The type of crime to be mentioned in the script.
        script (str): The script content to be used.

    Returns:
        dict: The API response or an error message.
    """
    # Defining the host is optional and defaults to https://api.callchimp.ai/v1
    # See configuration.py for a list of all supported configuration parameters.
    configuration = callchimp.Configuration(
        host="https://api.callchimp.ai/v1"
    )

    # Configure API key authorization: x-api-key
    api_key = os.getenv("API_KEY")
    if not api_key:
        return {"error": "API_KEY not found in environment variables"}

    configuration.api_key['x-api-key'] = api_key

    # Enter a context with an instance of the API client
    with callchimp.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = ScriptsApi(api_client)
        script_id = 263  # int | Numeric Script Id
        script_request = {
            "name": "Callchimp script",
            "script": f"""Hello, this is Dashabhuja, I’m calling to inform you about a {crime_type} case that has been reported in your jurisdiction. Would you like to learn more about the case?"
            
If user responds in an affirmative way, please respond “{script}. It’s important that this matter is addressed promptly to ensure the safety of all involved parties. Would you like to receive a detailed description of the case?”
            
But if the user responds in a negative way, Okay, I will keep you updated if I come across more severe cases. Your vigilance is crucial for community safety. Goodbye."
            
After this, if the user responds in an affirmative way, please respond "A link with the detailed description of the case has been sent to your mobile. Please review it at your earliest convenience.”
            
But, if the user responds in a negative way, please respond “Okay, I will keep you updated if I come across more severe cases. Your vigilance is crucial for community safety. Goodbye.”"""
        }

        try:
            # Update Script by Id
            api_response = api_instance.scripts_update(script_id, script_request)
            print("The response of ScriptsApi->scripts_update:\n")
            pprint(api_response)
            return api_response
        except ApiException as e:
            print(f"Exception when calling ScriptsApi->scripts_update: {e}\n")
            return {"error": f"{e} Script not updated, check scriptupdater function."}
#this is for testing purpose and needed to be reomved for full intergration

