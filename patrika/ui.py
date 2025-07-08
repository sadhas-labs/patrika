import streamlit as st
import pandas as pd
from patrika.core import send_email, load_sent_emails, record_sent_email


def run_ui():
    st.title("📮 Patrika - Sabha Email Sender")

    uploaded_csv = st.file_uploader("Upload Sabha Email List (CSV with 'Email' column)", type=["csv"])

    st.subheader("Your Details")
    sender_name = st.text_input("Your Name", placeholder="Srihari Raman")
    teacher_name = st.text_input("Your Guru's Name", placeholder="Sri. Tiruvarur Vaidyanathan")
    from_date = st.date_input("Available From (e.g., December 23, 2023)")
    to_date = st.date_input("Available Until (e.g., January 1, 2024)")

    st.subheader("Customize Your Message")
    subject_input = st.text_input("Subject", placeholder="Requesting a Mridangam Opportunity - December Music Season")
    body_template = st.text_area("Body Template", height=250, value=
    f"""Dear Respected Sir/Madam,

My name is {{name}}, and I am a disciple of {{guru}}.

I am requesting an opportunity to perform in your esteemed sabha during the December Music Season. I will be available from {{from_date}} to {{to_date}} and would be honored to be considered.

Namaste,
{{name}}""")

    uploaded_pdf = st.file_uploader("Upload Bio (PDF)", type=["pdf"])

    if uploaded_csv and uploaded_pdf and st.button("Send Emails"):
        df = pd.read_csv(uploaded_csv)
        emails = df["Email"].dropna().tolist()
        sent = load_sent_emails()
        to_send = [e for e in emails if e not in sent]

        with st.spinner(f"Sending {len(to_send)} emails..."):
            for email in to_send:
                body = body_template.format(
                    name=sender_name,
                    guru=teacher_name,
                    from_date=from_date.strftime("%B %d, %Y"),
                    to_date=to_date.strftime("%B %d, %Y")
                )
                try:
                    send_email(email, subject_input, body, uploaded_pdf)
                    record_sent_email(email, status="sent")
                except Exception as e:
                    record_sent_email(email, status="failed")
                    st.error(f"Failed to send to {email}: {str(e)}")

        st.success("Email dispatch complete.")
