import streamlit as st
from botocore.exceptions import ClientError
from utils.aws import get_sns_client, unsubscribe_from_topic

st.title("🚫 Unsubscribe from CVE Alerts")
st.write("Enter your Subscription ARN to stop receiving alerts.")

st.info(
    "💡 Your Subscription ARN was sent to you in the confirmation email/message "
    "you received after subscribing. It looks like:\n\n"
    "`arn:aws:sns:us-east-1:732481404831:avd-high-value-cve-alerts:abc123-def456-ghi789`"
)

subscription_arn = st.text_input(
    "Subscription ARN",
    placeholder="e.g. arn:aws:sns:us-east-1:732481404831:avd-high-value-cve-alerts:abc-123-def",
)

if st.button("Unsubscribe", type="primary"):
    if not subscription_arn.strip():
        st.error("Subscription ARN cannot be empty.")
    elif not subscription_arn.startswith("arn:aws:sns:"):
        st.error("Invalid ARN. It must start with arn:aws:sns:")
    else:
        try:
            sns = get_sns_client(
                st.secrets["AWS_ACCESS_KEY_ID"],
                st.secrets["AWS_SECRET_ACCESS_KEY"],
                st.secrets["AWS_REGION"],
                st.secrets["AWS_ROLE_ARN"],
            )
            unsubscribe_from_topic(sns, subscription_arn)
            st.success("✅ You have been unsubscribed from CVE alerts.")
        except ClientError as e:
            st.error(f"❌ Failed to unsubscribe: {e.response['Error']['Message']}")
