import smtplib
from email.message import EmailMessage

def send_test_email(smtp_server, smtp_port, sender_email, receiver_email, username, password):
    # Create a message object
    message = EmailMessage()
    message['Subject'] = 'SMTP Test Email'
    message['From'] = sender_email
    message['To'] = receiver_email
    message.set_content('This is a test email sent via SMTP.')

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start the TLS encryption
            server.starttls()
            # Login to the SMTP server
            server.login(username, password)
            # Send the email
            server.send_message(message)
        print('Test email sent successfully.')
    except Exception as e:
        print(f'Error sending the test email: {str(e)}')

# SMTP server details
smtp_server = 'example-smtp.com'
smtp_port = 587

# Sender and receiver email addresses
sender_email = 'sender@email.com'
receiver_email = 'receiver@email.com'

# SMTP server authentication credentials
username = 'smtp-username'
password = 'your-password'

# Send the test email
send_test_email(smtp_server, smtp_port, sender_email, receiver_email, username, password)
