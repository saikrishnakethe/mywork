import streamlit as st
from botocore.exceptions import ClientError
from utils.aws import get_sns_client, validate_endpoint, subscribe_to_topic

COUNTRY_CODES = [
    ("🇮🇳 +91 (India)", "+91"),
    ("🇺🇸 +1 (US)", "+1"),
    ("🇬🇧 +44 (UK)", "+44"),
    ("🇦🇺 +61 (Australia)", "+61"),
    ("🇩🇪 +49 (Germany)", "+49"),
    ("🇸🇬 +65 (Singapore)", "+65"),
]

PROTOCOLS = ["email", "sms", "http", "https", "sqs", "lambda"]

PLACEHOLDERS = {
    "email": "e.g. john.doe@company.com",
    "http": "e.g. http://myserver.com/alerts",
    "https": "e.g. https://myserver.com/alerts",
    "sqs": "e.g. https://sqs.us-east-1.amazonaws.com/123456789012/my-queue",
    "lambda": "e.g. arn:aws:lambda:us-east-1:123456789012:function:my-function",
}

st.title("📧 Subscribe to CVE Alerts")
st.write("Fill in the form below to start receiving high-severity CVE alerts.")

protocol = st.selectbox("Protocol", PROTOCOLS)

phone_number = ""
endpoint = ""

if protocol == "sms":
    col1, col2 = st.columns([1, 2])
    with col1:
        country_labels = [c[0] for c in COUNTRY_CODES]
        idx = st.selectbox(
            "Country Code",
            range(len(COUNTRY_CODES)),
            format_func=lambda i: country_labels[i],
        )
        country_code = COUNTRY_CODES[idx][1]
    with col2:
        phone_number = st.text_input("Phone Number", placeholder="e.g. 9876543210")
    endpoint = f"{country_code}{phone_number}"
else:
    endpoint = st.text_input("Endpoint", placeholder=PLACEHOLDERS.get(protocol, ""))

if st.button("Subscribe", type="primary"):
    value_to_validate = phone_number if protocol == "sms" else endpoint
    is_valid, error_msg = validate_endpoint(protocol, value_to_validate)
    if not is_valid:
        st.error(error_msg)
    else:
        try:
            sns = get_sns_client(
                st.secrets["AWS_ACCESS_KEY_ID"],
                st.secrets["AWS_SECRET_ACCESS_KEY"],
                st.secrets["AWS_REGION"],
                st.secrets["AWS_ROLE_ARN"],
            )
            arn = subscribe_to_topic(sns, st.secrets["SNS_TOPIC_ARN"], protocol, endpoint)
            if protocol == "email":
                st.success("✅ Subscribed! Check your email to confirm the subscription.")
            elif protocol == "sms":
                st.success("✅ Subscribed! You will receive a confirmation SMS shortly.")
            else:
                st.success(f"✅ Subscribed successfully!\n\nYour Subscription ARN: `{arn}`")
        except ClientError as e:
            st.error(f"❌ Failed to subscribe: {e.response['Error']['Message']}")
