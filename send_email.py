import yagmail
import os

def send_email():
    # Get credentials from environment variables
    email_user = os.getenv('GMAIL_USER')
    email_password = os.getenv('GMAIL_PASS')

    # Set up the email client
    yag = yagmail.SMTP(email_user, email_password)

    # Send the email with the attached report
    yag.send(
        to='recipient@example.com',
        subject='Weekly GitHub Activity Report',
        contents='Attached is your weekly activity report.',
        attachments='path/to/generated_report.html'  # Adjust to the generated report file path
    )

if __name__ == "__main__":
    send_email()
