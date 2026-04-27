import boto3
from botocore.exceptions import ClientError


def get_sns_client(access_key: str, secret_key: str, region: str, role_arn: str):
    sts = boto3.client(
        "sts",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )
    assumed = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="streamlit-cve-alerts",
    )
    creds = assumed["Credentials"]
    return boto3.client(
        "sns",
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
        region_name=region,
    )


def validate_endpoint(protocol: str, endpoint: str) -> tuple:
    if not endpoint.strip():
        return False, "Endpoint cannot be empty."
    if protocol == "email":
        parts = endpoint.split("@")
        if len(parts) != 2 or "." not in parts[1]:
            return False, "Enter a valid email address."
    elif protocol == "sms":
        digits = endpoint.strip()
        if not digits.isdigit():
            return False, "Phone number must contain digits only."
        if not (7 <= len(digits) <= 15):
            return False, "Phone number must be 7–15 digits long."
    elif protocol == "http":
        if not endpoint.startswith("http://"):
            return False, "URL must start with http://"
    elif protocol == "https":
        if not endpoint.startswith("https://"):
            return False, "URL must start with https://"
    elif protocol == "sqs":
        if not endpoint.startswith("https://sqs."):
            return False, "SQS URL must start with https://sqs."
    elif protocol == "lambda":
        if not endpoint.startswith("arn:aws:lambda:"):
            return False, "Lambda ARN must start with arn:aws:lambda:"
    return True, ""


def subscribe_to_topic(sns_client, topic_arn: str, protocol: str, endpoint: str) -> str:
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol=protocol,
        Endpoint=endpoint,
        ReturnSubscriptionArn=True,
    )
    return response["SubscriptionArn"]


def unsubscribe_from_topic(sns_client, subscription_arn: str) -> None:
    sns_client.unsubscribe(SubscriptionArn=subscription_arn)
