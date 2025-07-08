import smtplib
import ssl
import logging
import csv
from email.message import EmailMessage
from pathlib import Path
from datetime import datetime
import pandas as pd
from patrika.config import SENDER_EMAIL, EMAIL_PASSWORD

# Setup logging
logging.basicConfig(
    filename='patrika.log',
    filemode='a',
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO
)

# Constants
HISTORY_FILE = "sent_history.csv"


# --- Email history handling ---
def load_sent_emails():
    """Load emails marked as 'sent' in the history CSV."""
    if not Path(HISTORY_FILE).exists():
        return set()
    with open(HISTORY_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return {row['email'] for row in reader if row['status'] == 'sent'}


def record_sent_email(email, status):
    """Append an entry to the email history log."""
    with open(HISTORY_FILE, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['email', 'status', 'timestamp'])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'email': email,
            'status': status,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    logging.info(f"Email to {email} marked as '{status}'.")


# --- Email sending logic ---

def send_email(receiver_email, subject, body, attachment_file):
    """
    Send an email with the given subject, body, and attachment (PDF).
    """
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg.set_content(body)

    # Attach PDF
    file_data = attachment_file.read()
    file_name = attachment_file.name
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    # Send it securely
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)

    logging.info(f"Email successfully sent to {receiver_email}")


# --- CSV Reader ---

def get_emails(csv_path):
    """
    Accepts a path to a CSV file with an 'Email' column.
    Returns a list of valid email addresses.
    """
    df = pd.read_csv(csv_path)
    if "Email" not in df.columns:
        raise ValueError("CSV must contain an 'Email' column.")
    emails = df["Email"].dropna().tolist()
    logging.info(f"Loaded {len(emails)} email(s) from {csv_path}")
    return emails
