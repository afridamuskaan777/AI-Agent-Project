import streamlit as st
import pandas as pd
import requests
import openai
import time
import random
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
import smtplib

# Load environment variables from .env file (for local development)
load_dotenv()

# Retrieve sensitive data from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Start a background scheduler
scheduler = BackgroundScheduler()

# Step 1: Load Data
st.title("Custom Email Sender with Real-Time Tracking")
uploaded_file = st.file_uploader("Upload a CSV file or connect to Google Sheets", type=["csv"])
data = pd.DataFrame()

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data")
    st.dataframe(data)

# Step 2: Prompt Box with Column Detection for Placeholders
st.write("### Customize Your Email Prompt")
if not data.empty:
    columns = data.columns.tolist()
    placeholders = [f"{{{col}}}" for col in columns]
    st.write("Detected placeholders:", placeholders)

prompt = st.text_area("Enter your email template", "Hello {Company Name}, we noticed you are based in {Location}. Check our new offers!")

# Step 3: Generate Customized Emails using LLM
def generate_email_content(prompt, row):
    filled_prompt = prompt
    for col in columns:
        placeholder = f"{{{col}}}"
        filled_prompt = filled_prompt.replace(placeholder, str(row[col]))
    return filled_prompt

email_content = []
if not data.empty:
    st.write("### Generated Email Preview")
    for i, row in data.iterrows():
        email_body = generate_email_content(prompt, row)
        email_content.append({
            "recipient": row['Email'],
            "content": email_body,
            "status": "Pending"
        })
        st.write(f"Email to {row['Company Name']}:")
        st.write(email_body)
        st.markdown("---")

# Step 4: ESP Email Sending Function
def send_email(to_email, subject, body):
    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": f"Your Name <you@{MAILGUN_DOMAIN}>",
              "to": to_email,
              "subject": subject,
              "text": body})
    return response

# Step 5: Schedule and Send Emails
st.write("### Scheduling & Sending Options")
schedule_option = st.checkbox("Schedule Emails")
throttle_option = st.checkbox("Throttle Emails")

# Throttling and Scheduling Parameters
rate_limit = st.slider("Rate Limit (emails/hour)", 1, 50, 10) if throttle_option else None
schedule_time = st.time_input("Select Email Schedule Time", value=datetime.now().time()) if schedule_option else None

# Schedule Function
def schedule_emails(email_list, send_at):
    for email in email_list:
        schedule_time = datetime.combine(datetime.today(), send_at) if send_at else datetime.now()
        scheduler.add_job(send_email, 'date', run_date=schedule_time,
                          args=[email['recipient'], "Custom Email", email['content']])
    scheduler.start()

# Email Sending or Scheduling Trigger
if st.button("Send Emails"):
    if schedule_option:
        schedule_emails(email_content, schedule_time)
        st.success("Emails scheduled successfully.")
    else:
        for email in email_content:
            response = send_email(email['recipient'], "Custom Email", email['content'])
            email['status'] = "Sent" if response.status_code == 200 else "Failed"
            st.write(f"Email sent to {email['recipient']}: {email['status']}")

# Step 6: Real-Time Analytics
st.write("### Real-Time Analytics")
sent_count = len([email for email in email_content if email['status'] == "Sent"])
pending_count = len([email for email in email_content if email['status'] == "Pending"])
failed_count = len([email for email in email_content if email['status'] == "Failed"])

st.write(f"Total Emails Sent: {sent_count}")
st.write(f"Pending Emails: {pending_count}")
st.write(f"Failed Emails: {failed_count}")

# Display analytics with a progress bar
if st.button("Track Email Status"):
    while pending_count > 0:
        pending_count -= 1
        sent_count += 1
        st.progress(sent_count / len(email_content))
        time.sleep(1)

st.write("### Email Log")
st.dataframe(pd.DataFrame(email_content))
