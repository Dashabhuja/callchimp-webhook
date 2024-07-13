# coding: utf-8

# flake8: noqa
"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 9 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks   - Scripts   - Voices  ## API Operations✅ ### Campaign Operations    - List Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id   - Search Campaign by Name or Id  ### Supervisor Operations    - List Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Supervisor by Id   - Verify Supervisor OTP by Id  ### List Operations    - List Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id   - Search List by Name or Id   - Create Campaign with Default List  ### Subscriber Operations    - List Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id   - Get Subscriber by Vendor Lead Code   - Delete Subscriber by Vendor Lead Code   - Update Subscriber by Vendor Lead Code  ### Call Operations    - List Calls   - Create a Call   - Get Call by Id   - List Supervisor Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ### Script Operations    - List Scripts   - Create a Script   - Get Script by Id   - Delete Script by Id   - Update Script by Id  ### Voice Operations   - List Available Voices  ## Authentication🔐 Callchimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` tab.   5. Click on `Create` button, add a name and an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from callchimp.models.call_list_response import CallListResponse
from callchimp.models.call_report_request import CallReportRequest
from callchimp.models.call_report_response import CallReportResponse
from callchimp.models.call_report_response_answered_calls import CallReportResponseAnsweredCalls
from callchimp.models.call_report_response_stats_inner import CallReportResponseStatsInner
from callchimp.models.call_request_by_lead_id import CallRequestByLeadId
from callchimp.models.call_request_by_vendor_lead_code import CallRequestByVendorLeadCode
from callchimp.models.call_response import CallResponse
from callchimp.models.calls_post_request import CallsPostRequest
from callchimp.models.campaign_add_super_request import CampaignAddSuperRequest
from callchimp.models.campaign_add_super_response import CampaignAddSuperResponse
from callchimp.models.campaign_find_request import CampaignFindRequest
from callchimp.models.campaign_list_response import CampaignListResponse
from callchimp.models.campaign_lists_request import CampaignListsRequest
from callchimp.models.campaign_remove_super_request import CampaignRemoveSuperRequest
from callchimp.models.campaign_remove_super_response import CampaignRemoveSuperResponse
from callchimp.models.campaign_request import CampaignRequest
from callchimp.models.campaign_response import CampaignResponse
from callchimp.models.campaign_update_request import CampaignUpdateRequest
from callchimp.models.campaign_upload_audio_response import CampaignUploadAudioResponse
from callchimp.models.inbound_call_list_response import InboundCallListResponse
from callchimp.models.inbound_call_response import InboundCallResponse
from callchimp.models.inbound_call_response_callchimp_number import InboundCallResponseCallchimpNumber
from callchimp.models.inbound_call_response_supervisor import InboundCallResponseSupervisor
from callchimp.models.list_find_request import ListFindRequest
from callchimp.models.lists_list_response import ListsListResponse
from callchimp.models.lists_request import ListsRequest
from callchimp.models.lists_response import ListsResponse
from callchimp.models.model4_xx_response import Model4XXResponse
from callchimp.models.model4_xx_response_errors_inner import Model4XXResponseErrorsInner
from callchimp.models.phone_number_list_response import PhoneNumberListResponse
from callchimp.models.phone_number_response import PhoneNumberResponse
from callchimp.models.script_list_response import ScriptListResponse
from callchimp.models.script_request import ScriptRequest
from callchimp.models.script_response import ScriptResponse
from callchimp.models.subscriber_list_response import SubscriberListResponse
from callchimp.models.subscriber_request import SubscriberRequest
from callchimp.models.subscriber_response import SubscriberResponse
from callchimp.models.subscriber_update_request import SubscriberUpdateRequest
from callchimp.models.subscribers_post200_response import SubscribersPost200Response
from callchimp.models.subscribers_post_request import SubscribersPostRequest
from callchimp.models.supervisor_list_response import SupervisorListResponse
from callchimp.models.supervisor_request import SupervisorRequest
from callchimp.models.supervisor_response import SupervisorResponse
from callchimp.models.supervisor_send_otp_response import SupervisorSendOtpResponse
from callchimp.models.supervisor_verify_otp_request import SupervisorVerifyOtpRequest
from callchimp.models.supervisor_verify_otp_response import SupervisorVerifyOtpResponse
from callchimp.models.transaction_call_request_by_lead_id import TransactionCallRequestByLeadId
from callchimp.models.voice_response import VoiceResponse
from callchimp.models.webhook_list_response import WebhookListResponse
from callchimp.models.webhook_request import WebhookRequest
from callchimp.models.webhook_response import WebhookResponse
