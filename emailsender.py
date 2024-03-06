import os
from email.message import EmailMessage

email_sender = 'siabmsiasbm@gmail.com'
email.password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'siabmsiasbm@gmail.com'

subject = 'Test send'
body = """
Test send
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL('')