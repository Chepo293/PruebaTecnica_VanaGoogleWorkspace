from __future__ import print_function
import os.path
import re
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from httplib2 import GoogleLoginAuthentication
from googleapiclient.errors import HttpError

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
        
        # Create a client for the Admin SDK Directory API
        service = build('admin', 'directory_v1', credentials=creds)

        # List the groups in the directory
        results = service.groups().list(customer='my_customer', orderBy='email').execute()

        if 'groups' in results:
            group_data = results['groups']
            print("Groups Keys in the directory:")
            for group in group_data:
                email = group['email']
                groupName = group['name']
                print(f"*Name: {groupName}, Email Group: {email}")

            email_group = input("Enter the group to be queried:")
            if not validate_domain_email(email_group):
                print(f"::ERROR:: {email} is not a valid email from pruebavana.com")    
                return  
            
            not_found_email = True
            for group in group_data:
                if email_group == group['email']:
                    not_found_email = False
                    break

            if not_found_email:
                print(f"The email {email_group} does not belong to any group")
                return                    

            # List the members of the group
            result = service.members().list(groupKey=email_group).execute()

            if 'members' in result:
                print(f'Members of the group {email_group}:')
                for member in result['members']:
                    print(f'* Email: {member["email"]}')
        else:
            print("No groups were found in the directory.")
            
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