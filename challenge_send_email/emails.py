#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import os.path
import smtplib, ssl

def generate_email(sender, recipient, subject, body, attachment_path):
    # Basic Email formatting
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
    return message

def generate_error_report(sender, recipient, subject, body):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    # Create secure connection with mail server and send email

    # if You will use GMAIL
    # ENABLE IMAP in gmail account -> read https://support.google.com/mail/?p=BadCredentials
    # ENABLE 2FA then Generate an App Password -> https://myaccount.google.com/apppasswords
    # use the generated app paswword on your app.

    sender_email = input("Type your SENDER EMAIL and press enter:")
    receiver_email = input("Type your RECEIVER EMAIL and press enter:")
    password = input("Type your password and press enter:")

    host="smtp.gmail.com"
    port=465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        try:
            server.login(sender_email, password)
            print("GMAIL Login Success. Now Sending ...")
        except:
            print("LOGIN ERROR")

        try:
            server.send_message(message,sender_email,receiver_email)
            print("*** EMAIL SENT ****")
        except:
            print("ERROR IN SENDING")

        server.quit()