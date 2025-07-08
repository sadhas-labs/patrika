import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

CURRENT_YEAR = datetime.now().year
NEXT_YEAR = CURRENT_YEAR + 1
FIRST_DATE = f"December 23, {CURRENT_YEAR}"
LAST_DATE = f"January 1, {NEXT_YEAR}"

SUBJECT = f"December Music Season {CURRENT_YEAR} - Srihari Raman - Mridangam - Requesting an Opportunity to Perform"
BODY = f"""
Dear Respected Sir/Madam,

My name is Srihari Raman, and I am a disciple of Kalaimamani Guru Sri. Tiruvarur Vaidyanathan Sir.

I am sending this email asking for an opportunity during the December Music Season of {CURRENT_YEAR} - {NEXT_YEAR}, and I have attached my short bio for your review. Participating in this remarkable time of the year in an esteemed sabha like yours would be great.

I will be in India from {FIRST_DATE} to {LAST_DATE}, and I am looking forward to performing in your sabha.

Namaste,

Srihari Raman
"""
