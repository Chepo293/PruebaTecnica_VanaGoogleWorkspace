from __future__ import print_function
import os.path
import sys
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from httplib2 import GoogleLoginAuthentication

# Define the necessary scope for Google Directory API
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']

def validate_domain_email(email):
    # Regular expression pattern to validate a specific domain
    pattern = r'^[a-zA-Z0-9._%+-]+@pruebavana\.com$'

    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

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

        # Request user input for group information
        email = input("Enter the group email (example@pruebavana.com):")
        if not validate_domain_email(email):
            print(f"::ERROR:: {email} is not a valid email from pruebavana.com")    
            return    
        nameGroup = input("Now the group name:")
        description = input("Finally a brief description:")
        print('::WARNING:: Group names and emails cannot be repeated in the list')

        # Create a client for the Admin SDK Directory API
        service = build('admin', 'directory_v1', credentials=creds)
        
        # List existing groups in the directory
        groups = service.groups().list(customer='my_customer').execute()

        if 'groups' in groups:
            for group in groups['groups']:
                # Check if there is a group with the same name or email
                if group['name'].lower() == nameGroup.lower():
                    print('::ERROR:: There is already a group with that name, try another one.')
                    return 
                elif (group['email'].lower() == email.lower()):
                    print('::ERROR:: The email has already been assigned to a group.')
                    return 

        # Create a dictionary for the new group
        new_group = {
            "email": email,
            "name": nameGroup,
            "description": description
        }

        # Insert the new group into the directory
        result = service.groups().insert(body=new_group).execute()

        if result:
            print("\n==========================================================")
            print(f'::SUCCESS:: Group "{nameGroup}" created successfully')
            print("==========================================================\n")

        else:
            print("\n==========================================================")
            print('::FAIL:: Group creation failed')
            print("==========================================================\n")
            
    except google_auth_oauthlib.auth.exceptions.DefaultCredentialsError:
        print("Default credentials were not found. Make sure the credentials are set correctly.")
    except GoogleLoginAuthentication.auth.exceptions.RefreshError:
        print("Error updating credentials. You must authorize the application again.")
    except (OSError, FileNotFoundError):
        print("Could not open or read file 'token.json'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()