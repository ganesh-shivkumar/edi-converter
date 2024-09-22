import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

#Scopes which are required for Generative API calls.
SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever','https://www.googleapis.com/auth/generative-language.tuning']

def load_creds():
    creds = None

    # If the token json is already present, get the creds for the scopes defined.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        # If the credentials are expired, refresh the token
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #Get the credentials from the client secret json
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # From the token json, get the credentials.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds