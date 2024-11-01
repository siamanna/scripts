import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_custom_email():
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "your_email@gmail.com"  # Replace with your email
    email_password = "your_password"  # Replace with your email password or use environment variables

    try:
        # Number of recipients
        num_recipients = int(input("Enter the number of recipients: "))

        recipients = []
        for i in range(num_recipients):
            recipient_email = input(f"Enter the email address for recipient {i + 1}: ")
            recipients.append(recipient_email)

        # Subject and body
        subject = input("Enter the subject of the email: ")
        body = input("Enter the body of the email: ")

        # Attachment
        attachment_response = input("Do you want to add an attachment? (yes/no): ").strip().lower()
        attachment_path = None

        if attachment_response == "yes":
            attachment_path = input("Enter the file path of the attachment: ")
            if not os.path.isfile(attachment_path):
                print("Attachment file not found.")
                return

        # Establish SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable encryption for security
            server.login(email_address, email_password)

            # Create email for each recipient
            for recipient in recipients:
                msg = MIMEMultipart()
                msg["From"] = email_address
                msg["To"] = recipient
                msg["Subject"] = subject

                # Attach the email body
                msg.attach(MIMEText(body, "plain"))

                # Attach the file, if specified
                if attachment_path:
                    with open(attachment_path, "rb") as attachment_file:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment_file.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(attachment_path)}",
                    )
                    msg.attach(part)

                # Send the email
                server.sendmail(email_address, recipient, msg.as_string())
                print(f"Email sent to: {recipient}")

        print("Emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
send_custom_email()
