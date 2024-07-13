# coding: utf-8

"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 9 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks   - Scripts   - Voices  ## API Operations✅ ### Campaign Operations    - List Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id   - Search Campaign by Name or Id  ### Supervisor Operations    - List Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Supervisor by Id   - Verify Supervisor OTP by Id  ### List Operations    - List Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id   - Search List by Name or Id   - Create Campaign with Default List  ### Subscriber Operations    - List Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id   - Get Subscriber by Vendor Lead Code   - Delete Subscriber by Vendor Lead Code   - Update Subscriber by Vendor Lead Code  ### Call Operations    - List Calls   - Create a Call   - Get Call by Id   - List Supervisor Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ### Script Operations    - List Scripts   - Create a Script   - Get Script by Id   - Delete Script by Id   - Update Script by Id  ### Voice Operations   - List Available Voices  ## Authentication🔐 Callchimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` tab.   5. Click on `Create` button, add a name and an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from callchimp.models.lists_response import ListsResponse

class TestListsResponse(unittest.TestCase):
    """ListsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListsResponse:
        """Test ListsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListsResponse`
        """
        model = ListsResponse()
        if include_optional:
            return ListsResponse(
                added_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                campaign = 56,
                description = '',
                id = 56,
                isactive = True,
                isauto = True,
                name = '',
                organization = 56
            )
        else:
            return ListsResponse(
        )
        """

    def testListsResponse(self):
        """Test ListsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
