import streamlit as st

st.set_page_config(
    page_title="CVE Alerts Subscription",
    page_icon="🔔",
    layout="centered",
)

st.title("🔔 CVE Alerts Subscription")
st.markdown(
    """
    Welcome to the **CVE Alerts** subscription portal.

    Use the sidebar to navigate:

    - 📧 **Subscribe** — add your email, phone, or endpoint to receive alerts
    - 🚫 **Unsubscribe** — remove yourself from the alerts list
    - ℹ️ **About Alerts** — learn what types of alerts you will receive

    ---

    This portal connects you to the **high-severity CVE alerting pipeline**, which monitors:
    - National Vulnerability Database (NVD)
    - Apache Struts Security Bulletins
    - Security blog coverage of active CVEs
    """
)
