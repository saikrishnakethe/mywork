import streamlit as st

st.title("ℹ️ About the Alerts")
st.write("Once subscribed, you will receive **2 types of alerts** from this topic:")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background:#fff3e0;border-left:4px solid #e05c2a;padding:1rem;
                    border-radius:6px;min-height:160px">
        <h4 style="margin-top:0">🔴 Source Alerts</h4>
        <p style="font-size:0.85rem;color:#555;margin-bottom:0">
        High-severity alerts from security sources including NVD (National Vulnerability Database),
        Apache Struts bulletins, and other sources added over time.<br/><br/>
        <b>Includes:</b> CVE ID, CVSS score, severity, affected versions, solution links.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="background:#e3f2fd;border-left:4px solid #1976d2;padding:1rem;
                    border-radius:6px;min-height:160px">
        <h4 style="margin-top:0">📰 Blog Alerts</h4>
        <p style="font-size:0.85rem;color:#555;margin-bottom:0">
        Alerts when a CVE is actively discussed in security blogs and research articles.<br/><br/>
        <b>Includes:</b> CVE ID, blog source name, article title, URL, published date.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.markdown(
    """
### Protocols Explained

| Protocol | Use when |
|----------|----------|
| **email** | You want alerts delivered to your inbox |
| **sms** | You want text message alerts on your phone |
| **https** | You have a webhook endpoint (Slack, PagerDuty, etc.) |
| **http** | You have an HTTP endpoint (non-SSL) |
| **sqs** | You have an AWS SQS queue to receive and process alerts |
| **lambda** | You have an AWS Lambda function to process alerts programmatically |
    """
)
