import requests
from bs4 import BeautifulSoup
import json
import time
import os.path
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# URLs to scrape
mens_sunglasses_url = "https://www.sunglasshut.com/ca-en/mens-sunglassesCID=intlmod"
womens_sunglasses_url = "https://www.sunglasshut.com/ca-en/womens-sunglasses"

def send_email_alert(new_items):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    sender_email = "******@gmail.com"
    receiver_email = "*******@gmail.com"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Sunglasses Alert"
    
    body = "New sunglasses in stock:\n\n" + "\n".join(new_items)
    msg.attach(MIMEText(body, 'plain'))
    
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    message = {'raw': raw}

    try:
        message = (service.users().messages().send(userId="me", body=message)
                   .execute())
        print(f"Message Id: {message['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")

# Function to scrape sunglasses data
def scrape_sunglasses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sunglasses = soup.find_all('div', class_='product-tile')
    items = []
    for sunglass in sunglasses:
        name = sunglass.find('span', class_='product-title').text.strip()
        items.append(name)
    return items

# Main function to check for new sunglasses
def check_for_new_sunglasses():
    mens_sunglasses = scrape_sunglasses(mens_sunglasses_url)
    womens_sunglasses = scrape_sunglasses(womens_sunglasses_url)
    
    try:
        with open('sunglasses_data.json', 'r') as file:
            old_data = json.load(file)
    except FileNotFoundError:
        old_data = {"mens": [], "womens": []}
    
    new_mens_sunglasses = set(mens_sunglasses) - set(old_data["mens"])
    new_womens_sunglasses = set(womens_sunglasses) - set(old_data["womens"])
    
    new_items = list(new_mens_sunglasses) + list(new_womens_sunglasses)
    
    if new_items:
        print("New items found:", new_items)
        send_email_alert(new_items)
    else:
        print("No new items found.")
    
    with open('sunglasses_data.json', 'w') as file:
        json.dump({"mens": mens_sunglasses, "womens": womens_sunglasses}, file)

if __name__ == "__main__":
    while True:
        check_for_new_sunglasses()
        time.sleep(3600)  # Check every hour
