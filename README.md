# 📮 Patrika – Sabha Email Sender

**Patrika** is a simple and elegant email tool built with Python and Streamlit to help artists like Srihari Raman reach out to sabhas during the December Music Season.

This tool allows you to:

- Upload a CSV of sabha contact emails
- Customize your name, guru's name, date range, subject, and message
- Attach a PDF bio
- Automatically send personalized emails via your Gmail account

---

## 🚀 Features

- 📬 Bulk email sending with PDF attachment
- ✍️ Customizable email body with placeholders
- ✅ Tracks sent emails to avoid duplicates
- 🔒 Secure credential handling via `.env` file
- 🧾 Logs sent and failed emails in a CSV history file

---

## 🧰 Requirements

- Python 3.8+
- Gmail account with App Password
- `.csv` file with an `Email` column
- `.pdf` file of your bio

---

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/patrika.git
cd patrika
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
Clone the `.env.example` file and fill in your Gmail App credentials.

```bash
cp .env.example .env
```

### 4. Prepare your CSV and PDF files
- Create a CSV file with a column named `Email` containing the sabha email addresses.
- Prepare a PDF file of your bio.

### 5. Run the app

```bash
streamlit run app.py
```

# Contributions
Contributions are welcome! Please fork the repository and submit a pull request.

# License
This project is licensed under the MIT License. See the `LICENSE` file for details.

# Acknowledgements
Built by Srihari Raman with ❤️ using Python and Streamlit.
