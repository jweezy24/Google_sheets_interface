from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.scripts',
'https://www.googleapis.com/auth/drive.metadata', 'https://www.googleapis.com/auth/drive.photos.readonly', 'https://www.googleapis.com/auth/drive.file',
'https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/script.projects', 'https://www.googleapis.com/auth/spreadsheets']

def get_picture(pic_id):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
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

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    querey =  "name contains '"+ str(pic_id) + "'"
    print(querey)
    pictures = service.files().list(q=querey).execute()

    print(pictures)

    if not pictures:
        print('No files found.')
    else:
        print('Files:')
        for pic in pictures['files']:
            drive_link = u'https://drive.google.com/file/d/{0}/view?usp=sharing'.format(pic['id'])
        return drive_link

if __name__ == '__main__':
    print(get_picture("IMG_5263"))
