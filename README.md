<h1 align="center">📮 Patrika – Sabha Email Sender</h1>
<div align="center">
  <img src="/assets/patrika_logo.png" alt="Patrika Logo" width="180" style="margin-bottom: 10px; border-radius: 50%;" />

  <h2><em>A Smart Email Companion for Artists During December Season</em></h2>
</div>

---

**Patrika** is a beautifully simple and powerful email automation tool designed to help artists like *Srihari Raman* connect with sabhas during the prestigious **December Music Season** in Chennai.

🎶 Whether you're a seasoned performer or a rising star, Patrika saves time, adds polish, and helps you present your best self — directly in the inboxes of decision-makers.

---

## ✨ What Can Patrika Do?

* 📤 **Bulk-send** personalized emails with just a few clicks
* 📝 Customize fields like **your name**, **guru’s name**, **performance dates**, and **message body**
* 📎 Attach a **PDF bio** to every email
* ✅ Keep track of emails already sent (no embarrassing duplicates!)
* 🔐 Safely handle credentials using a `.env` file
* 📑 Automatically generate a **CSV history log** of sent and failed emails

---

## 🚀 Features at a Glance

| Feature                      | Description                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| 📬 **Bulk Sending**          | Send emails with PDF bios to multiple sabhas in one go                    |
| ✨ **Template Customization** | Fill in placeholders like `{{name}}` or `{{guru}}` to tailor your message |
| 🔄 **No Repeat Sends**       | Automatically avoids re-sending to already contacted sabhas               |
| 🛡️ **Secure Auth**          | Uses Gmail App Passwords stored securely                                  |
| 📊 **Export Logs**           | Keeps a detailed record of email delivery status                          |

---

## 🧰 What You'll Need

* ✅ Python 3.8+
* ✅ Gmail account with [App Password](https://support.google.com/accounts/answer/185833)
* ✅ A `.csv` file with an `Email` column
* ✅ Your bio as a `.pdf`

---

## ⚙️ Getting Started

### 🔁 1. Clone the Repo

```bash
git clone https://github.com/your-username/patrika.git
cd patrika
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 3. Set Up Your `.env` File

```bash
cp .env.example .env
```

Then add your Gmail credentials (App Password recommended) to the `.env` file.

### 📁 4. Prepare Your Files

* CSV: Make sure it has a column named `Email` with sabha contact emails.
* PDF: Prepare your concert bio or profile document.

### ▶️ 5. Run the App

```bash
streamlit run app.py
```

---

## 🤝 Contribute

Have ideas to improve Patrika? Found a bug?
We’d love your input! Feel free to fork the repo and submit a pull request.

---

## 📄 License

Licensed under the **MIT License**.
See the [`LICENSE`](./LICENSE) file for full details.

---

## 🙏 Acknowledgements

Built with ❤️ by **Srihari Raman**
Made with Python, Streamlit, and a passion for Carnatic music.

---