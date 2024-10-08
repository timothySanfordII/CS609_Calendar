import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

def get_calendar_events():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
    
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return []

    reminders = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        summary = event.get('summary', 'No Title')
        location = event.get('location', 'No Location')
        description = event.get('description', 'No Description')
        reminders.append({
            'summary': summary,
            'start': start,
            'end': end,
            'location': location,
            'description': description,
        })
    return reminders

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                   # Typically 587 for TLS or 465 for SSL
EMAIL_ADDRESS = 'your_email@example.com'  # Your email address
EMAIL_PASSWORD = 'your_password'         # Your email password

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

# Get upcoming events and send reminders
events = get_calendar_events()
for event in events:
    subject = f'Reminder: {event["summary"]}'
    body = (f'Hello,\n\n'
            f'This is a reminder for your upcoming event:\n\n'
            f'Title: {event["summary"]}\n'
            f'Start: {event["start"]}\n'
            f'End: {event["end"]}\n'
            f'Location: {event["location"]}\n\n'
            f'Description:\n{event["description"]}\n\n'
            f'Best regards,\n'
            f'Your Calendar App')
    recipient_email = 'recipient@example.com'  # Replace with the recipient's email address
    send_email(subject, body, recipient_email)

print("Reminder emails sent successfully.")
