"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.
"""
from __future__ import print_function
import pickle
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_range():
    SCOPES = ['https://www.googleapis.com/auth/script.projects', 'https://www.googleapis.com/auth/spreadsheets']
    """Calls the Apps Script API.
    """
    creds = None
    scriptID = '17F_P-r3_9Ou0evcV2ldMKQbMn3zAJT18qQEZ7U2l1mdMELKl4GqJC-v8'
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./google_utils/token.pickle'):
        with open('./google_utils/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google_utils/credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('./google_utils/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('script', 'v1', credentials=creds)

    # Call the Apps Script API
    try:
        #Get the Script
        request = {
          "function": "ApplicationProject.get_range_fossil",
          "devMode": "true"
          }
        response = service.scripts().run(scriptId='17F_P-r3_9Ou0evcV2ldMKQbMn3zAJT18qQEZ7U2l1mdMELKl4GqJC-v8', body=request).execute()
        return response['response']['result']
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)


if __name__ == '__main__':
    print(get_range())
