import os
import callchimp
from callchimp.models.call_request_by_lead_id import CallRequestByLeadId
from callchimp.rest import ApiException
from callchimp.models.calls_post_request import CallsPostRequest
from dotenv import load_dotenv

load_dotenv()

def startcall():
    # Configure the API client
    configuration = callchimp.Configuration(
        host="https://api.callchimp.ai/v1"
    )
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY not found in environment variables")
        return

    configuration.api_key['x-api-key'] = api_key

    # Create an instance of the API client
    with callchimp.ApiClient(configuration) as api_client:
        # Assuming there's a method for CallRequestByLeadId, adjust as necessary
        api_instance = callchimp.CallsApi(api_client)
        call_request_by_lead_id_data = {"lead": 839678}  # Use the actual lead ID here
        
        call_request_by_lead_id = CallRequestByLeadId(**call_request_by_lead_id_data)
        calls_post_request_instance = CallsPostRequest(actual_instance=call_request_by_lead_id)
        
        try:
            # Use the CallsPostRequest instance with calls_post
            api_response = api_instance.calls_post(calls_post_request_instance)
            print("API Response:\n")
            print(api_response)
        except ApiException as e:
            print(f"ApiException when calling the API: {e}\n")
        except Exception as e:
            print(f"General Exception when calling the API: {e}\n")

