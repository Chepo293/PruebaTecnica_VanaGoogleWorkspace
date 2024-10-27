from __future__ import print_function

# Import required modules
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the necessary scope for Google Directory API
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']

def main():
    try:
        # Initialize credentials to null
        creds = None

        # Check if 'token.json' file with valid credentials exists
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no credentials or they are not valid, initiate the authentication process
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # Start the authentication flow using 'credentials.json' and the defined SCOPES
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for future runs in 'token.json'
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        # Create a client for the Admin SDK Directory API
        service = build('admin', 'directory_v1', credentials=creds)

        # List the groups in the directory
        results = service.groups().list(customer='my_customer', orderBy='email').execute()

        if 'groups' in results:
            group_data = results['groups']
            print("Groups Keys in the directory:")
            for group in group_data:
                groupKey = group['id']
                groupName = group['name']
                groupEmail = group['email']
                print(f"Group Key: {groupKey}, Name: {groupName}, Email: {groupEmail}")
        else:
            print("No groups were found in the directory.")
            
    except google_auth_oauthlib.auth.exceptions.DefaultCredentialsError:
        print("Default credentials were not found. Make sure the credentials are set correctly.")
    except google_auth_oauthlib.auth.exceptions.RefreshError:
        print("Error updating credentials. You must authorize the application again.")
    except (OSError, FileNotFoundError):
        print("Could not open or read file 'token.json'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()