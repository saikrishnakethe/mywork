import pytest
from unittest.mock import MagicMock
from utils.aws import validate_endpoint, subscribe_to_topic, unsubscribe_from_topic


class TestValidateEndpoint:
    def test_email_valid(self):
        ok, msg = validate_endpoint("email", "user@example.com")
        assert ok is True and msg == ""

    def test_email_missing_at(self):
        ok, msg = validate_endpoint("email", "notanemail")
        assert ok is False and "valid email" in msg

    def test_email_empty(self):
        ok, msg = validate_endpoint("email", "")
        assert ok is False and "empty" in msg

    def test_sms_valid(self):
        ok, msg = validate_endpoint("sms", "9876543210")
        assert ok is True and msg == ""

    def test_sms_too_short(self):
        ok, msg = validate_endpoint("sms", "123")
        assert ok is False and "7" in msg

    def test_sms_non_digits(self):
        ok, msg = validate_endpoint("sms", "98765abc10")
        assert ok is False and "digits" in msg

    def test_http_valid(self):
        ok, msg = validate_endpoint("http", "http://myserver.com/alerts")
        assert ok is True and msg == ""

    def test_http_wrong_scheme(self):
        ok, msg = validate_endpoint("http", "https://myserver.com")
        assert ok is False

    def test_https_valid(self):
        ok, msg = validate_endpoint("https", "https://myserver.com/alerts")
        assert ok is True and msg == ""

    def test_https_wrong_scheme(self):
        ok, msg = validate_endpoint("https", "http://myserver.com")
        assert ok is False

    def test_sqs_valid(self):
        ok, msg = validate_endpoint("sqs", "https://sqs.us-east-1.amazonaws.com/123/q")
        assert ok is True and msg == ""

    def test_sqs_invalid(self):
        ok, msg = validate_endpoint("sqs", "https://myserver.com/queue")
        assert ok is False

    def test_lambda_valid(self):
        ok, msg = validate_endpoint("lambda", "arn:aws:lambda:us-east-1:123:function:fn")
        assert ok is True and msg == ""

    def test_lambda_invalid(self):
        ok, msg = validate_endpoint("lambda", "arn:aws:s3:bucket")
        assert ok is False


class TestSubscribeToTopic:
    def test_returns_subscription_arn(self):
        mock_sns = MagicMock()
        mock_sns.subscribe.return_value = {
            "SubscriptionArn": "arn:aws:sns:us-east-1:123:topic:sub-abc"
        }
        result = subscribe_to_topic(
            mock_sns,
            "arn:aws:sns:us-east-1:123:topic",
            "email",
            "user@example.com",
        )
        assert result == "arn:aws:sns:us-east-1:123:topic:sub-abc"
        mock_sns.subscribe.assert_called_once_with(
            TopicArn="arn:aws:sns:us-east-1:123:topic",
            Protocol="email",
            Endpoint="user@example.com",
            ReturnSubscriptionArn=True,
        )


class TestUnsubscribeFromTopic:
    def test_calls_unsubscribe(self):
        mock_sns = MagicMock()
        unsubscribe_from_topic(mock_sns, "arn:aws:sns:us-east-1:123:topic:sub-abc")
        mock_sns.unsubscribe.assert_called_once_with(
            SubscriptionArn="arn:aws:sns:us-east-1:123:topic:sub-abc"
        )
