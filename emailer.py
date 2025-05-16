import smtplib, ssl
from email.message import EmailMessage
import json
import os

with open("config/settings.json") as f:
    config = json.load(f)

def send_email(transcript_path, summary_path):
    msg = EmailMessage()
    msg["Subject"] = "AIRA Call Summary"
    msg["From"] = config["email"]["from"]
    msg["To"] = config["email"]["to"]
    msg.set_content("Attached are the transcript and summary.")

    for path in [transcript_path, summary_path]:
        with open(path, "rb") as f:
            msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=os.path.basename(path))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(config["email"]["smtp"], config["email"]["port"], context=context) as server:
        server.login(config["email"]["from"], config["email"]["password"])
        server.send_message(msg)
