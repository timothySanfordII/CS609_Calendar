import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

def send_email(subject, body, to_email):
    # Email configuration
    from_email = 'sadewumi@wvstateu.edu'
    password = 'AfolayaN7*'  # Use an app password for Gmail

    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def create_reminder(event_name, event_time, reminder_time_minutes):
    # Calculate the reminder time
    reminder_time = event_time - timedelta(minutes=reminder_time_minutes)
    
    # Check if it's time to send the reminder
    if datetime.now() >= reminder_time:
        subject = f"Reminder: {event_name}"
        body = f"This is a reminder for your event: {event_name} at {event_time.strftime('%Y-%m-%d %H:%M:%S')}."
        send_email(subject, body, 'adewumisam07@gmail.com')

# Example usage
event_name = "Team Meeting"
event_time = datetime(2024, 9, 25, 14, 0)  # Set the event date and time
reminder_time_minutes = 30  # Reminder 30 minutes before

create_reminder(event_name, event_time, reminder_time_minutes)