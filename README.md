📲 WhatsApp Message Scheduler using Twilio

This Python project allows users to **schedule WhatsApp messages** to be sent at a specific future date and time using the Twilio API. It's ideal for sending birthday wishes, reminders, or any time-sensitive messages automatically.

✅ Features

* 🔒 Securely handles Twilio credentials using `.env` file
* 📥 Takes user input for recipient, message, and schedule time
* 🕰️ Schedules messages to be sent at a future date/time
* 📤 Sends WhatsApp messages using Twilio's official API


🛠️ Project Structure

```
1. Twilio Client Setup
2. User Inputs for recipient and message
3. Scheduling Logic using Python datetime
4. Message Dispatch using Twilio API
```

🧰 Requirements

* Python 3.6+
* Twilio account with WhatsApp Sandbox setup
* `twilio` Python module
* `python-dotenv` module

Install required packages:

```bash
pip install twilio python-dotenv
```

🔐 Setup Instructions

1. Clone the repository or download the script
2. Create a `.env` file** in the same directory and add:

   ```
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   ```
3. Ensure Twilio WhatsApp Sandbox is configured** [Twilio WhatsApp Setup Guide](https://www.twilio.com/docs/whatsapp/quickstart/python)

🚀 How to Run

1. Open your terminal or command prompt
2. Run the script:

   ```bash
   python whatsapp_scheduler.py
   ```
3. Provide the required inputs:

   * Recipient Name
   * WhatsApp number (with country code, e.g., +91XXXXXXXXXX)
   * Message content
   * Scheduled date (`YYYY-MM-DD`)
   * Scheduled time (`HH:MM` in 24-hour format)

🧪 Example

```
Enter the recipient name : Sakshi
Enter the recipient whatsapp no with country code : +9198XXXXXXXX
Enter the message you want to send to Sakshi : Don't forget to submit the project!
Enter the date to send the message (YYYY-MM-DD): 2025-07-01
Enter the time to send the message (HH:MM in 24 hours format): 14:30
```

> ✅ Output:
> Message scheduled to be sent to Sakshi at 2025-07-01 14:30:00
> (Message will be sent automatically at that time)

⚠️ Note

* Ensure the recipient number has joined the Twilio sandbox if you're using the trial account.
* Time is based on your local machine’s time zone.
* The script should remain running until the message is sent.

