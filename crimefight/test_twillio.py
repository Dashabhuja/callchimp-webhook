import unittest
from unittest.mock import patch
from twillio import send_twilio_message

class TestSendTwilioMessage(unittest.TestCase):
    @patch('twillio.Client')
    def test_send_twilio_message_success(self, mock_client):
        # Mock the Twilio client
        mock_message = mock_client.return_value.messages.create.return_value
        mock_message.sid = 'mock_sid'

        # Test data
        message_body = 'Test message'
        to_phone_number = '+1234567890'

        # Call the function
        send_twilio_message(message_body, to_phone_number)

        # Assert that the message was sent
        mock_client.assert_called_once_with('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
        mock_client.return_value.messages.create.assert_called_once_with(
            body=message_body,
            from_='TWILIO_PHONE_NUMBER',
            to=to_phone_number
        )
        self.assertEqual(mock_message.sid, 'mock_sid')

    @patch('twillio.Client')
    def test_send_twilio_message_failure(self, mock_client):
        # Mock the Twilio client to raise an exception
        mock_client.return_value.messages.create.side_effect = Exception('Test exception')

        # Test data
        message_body = 'Test message'
        to_phone_number = '+1234567890'

        # Call the function
        send_twilio_message(message_body, to_phone_number)

        # Assert that the exception was handled
        mock_client.assert_called_once_with('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
        mock_client.return_value.messages.create.assert_called_once_with(
            body=message_body,
            from_='TWILIO_PHONE_NUMBER',
            to=to_phone_number
        )

if __name__ == '__main__':
    unittest.main()