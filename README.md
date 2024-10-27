# PruebaTecnica_VanaGoogleWorkspace
## Google Workspace Python CLI Tool

## Overview

This Python CLI tool provides functionalities for managing Google Workspace using the Google Directory API. You can perform the following tasks:

- Add a user to a Google Workspace directory group.
- View all the aliases associated with a group.

## Project Structure

The project consists of the following files:

- `add_group.py`: Allows you to create groups in the Google Workspace directory.
- `add_member.py`: Enables the addition of users to directory groups.
- `list_groupAlias.py`: Lists all the members' aliases in a specified group.
- `list_groupKeys.py`: Lists all the groups in the Google Workspace directory.
- `token.json`: contains user-specific token data for authentication, this file was left as is for practical testing purposes.
- `credentials.json`: It stores the credentials to access the Google Directory API, as well as the token.json file, this file was left like this for practical testing purposes.

 
##### Important note: 
[Directory API](https://developers.google.com/admin-sdk/directory/v1/guides?hl=es_419) documentation was vital for the development of this tool.

## Prerequisites

Make sure you have the necessary credentials and token data, this can be found in the repository named token.json and credentials.json.

It is required to install or update the necessary Python packages to interact with Google APIs. This is a brief description of the installation dependencies.

1. google-api-python-client: This package provides a Python library to access and use Google APIs. It is essential to interact with Google services such as Google Workspace.

2. google-auth-httplib2: This package provides tools to authenticate HTTP requests made to the Google API. It helps handle user authentication, credential storage, and secure requests to Google APIs using the OAuth 2.0 protocol.

3. google-auth-oauthlib: This package complements google-auth-httplib2 and provides an additional authentication layer for OAuth 2.0-based authorization. Helps manage the credentials and authorization flows needed to access Google services securely.

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Usage
The project was created under the domain pruebavana.com for the purposes of this project.
### Create a new group
1. To create groups in the directory, it is necessary to execute the script with the python3 environment variable followed by the name of the script, it will immediately request the email to create the new group
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_group.py 
Enter the group email (example@pruebavana.com):
Now the group name:
```
2. After entering an email with a valid domain (@compravana.com) the group name will be requested
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_group.py 
Enter the group email (example@pruebavana.com):tests@pruebavana.com
Now the group name:
```
3.A brief description will be requested for the group that is being created.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_group.py 
Enter the group email (example@pruebavana.com):tests@pruebavana.com
Now the group name:Group Test
Finally a brief description:
```
4. After this, a warning will be generated saying that the names of the groups and their emails cannot be repeated in the directory. Finally, a message will be displayed indicating the successful creation of the group.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_group.py 
Enter the group email (example@pruebavana.com):test@pruebavana.com
Now the group name:Group Test
Finally a brief description:description of the group test.
::WARNING:: Group names and emails cannot be repeated in the list

==========================================================
::SUCCESS:: Group "Group Test" created successfully
==========================================================
```
### Create a new member
1. To create groups in the directory it is necessary to run the script with the python3 environment variable followed by the script name, the current groups will immediately be displayed so you can enter the email of the group to which you want to associate the new member.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_member.py 
Groups Keys in the directory:
	*Group Key: 01qoc8b12ngfk02, Name: Accounting group, Email: accounting@pruebavana.com
	*Group Key: 00sqyw644iawwjl, Name: Developers Gruop, Email: dev@pruebavana.com
	*Group Key: 0319y80a4gemd3q, Name: Quality Assurance, Email: qa@pruebavana.com
	*Group Key: 02grqrue0tt2qub, Name: Human Resources, Email: rrhh@pruebavana.com
	*Group Key: 01gf8i834htmd9d, Name: Sales Group, Email: sales_group@pruebavana.com
	*Group Key: 03vac5uf412nefh, Name: Group Test, Email: test@pruebavana.com
==========================================================================================

Enter the group email(example@pruebavana.com):
```
2. If the email entered is within the current groups, the email of the member who wants to associate with the group will be requested.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_member.py 
Groups Keys in the directory:
	*Group Key: 01qoc8b12ngfk02, Name: Accounting group, Email: accounting@pruebavana.com
	*Group Key: 00sqyw644iawwjl, Name: Developers Gruop, Email: dev@pruebavana.com
	*Group Key: 0319y80a4gemd3q, Name: Quality Assurance, Email: qa@pruebavana.com
	*Group Key: 02grqrue0tt2qub, Name: Human Resources, Email: rrhh@pruebavana.com
	*Group Key: 01gf8i834htmd9d, Name: Sales Group, Email: sales_group@pruebavana.com
	*Group Key: 03vac5uf412nefh, Name: Group Test, Email: test@pruebavana.com
==========================================================================================

Enter the group email(example@pruebavana.com):test@pruebavana.com
Enter the email member(example@pruebavana.com):
```
3.If the new member's email is correct (belonging to the domain pruebavana.com) a message is displayed indicating that the process was successful.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 add_member.py 
Groups Keys in the directory:
	*Group Key: 01qoc8b12ngfk02, Name: Accounting group, Email: accounting@pruebavana.com
	*Group Key: 00sqyw644iawwjl, Name: Developers Gruop, Email: dev@pruebavana.com
	*Group Key: 0319y80a4gemd3q, Name: Quality Assurance, Email: qa@pruebavana.com
	*Group Key: 02grqrue0tt2qub, Name: Human Resources, Email: rrhh@pruebavana.com
	*Group Key: 01gf8i834htmd9d, Name: Sales Group, Email: sales_group@pruebavana.com
	*Group Key: 03vac5uf412nefh, Name: Group Test, Email: test@pruebavana.com
==========================================================================================

Enter the group email(example@pruebavana.com):test@pruebavana.com
Enter the email member(example@pruebavana.com):usertest@pruebavana.com

==========================================================
::SUCCESS:: Member "usertest@pruebavana.com", added successfully
==========================================================
```
### List all groups in the directory
1. To know the group keys, names and email associated with each group, it is necessary to run the script with the python3 environment variable followed by the name of the script. This is an auxiliary script to be able to see how many groups have been created so far.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 list_groupKeys.py 
Groups Keys in the directory:
Group Key: 01qoc8b12ngfk02, Name: Accounting group, Email: accounting@pruebavana.com
Group Key: 00sqyw644iawwjl, Name: Developers Gruop, Email: dev@pruebavana.com
Group Key: 0319y80a4gemd3q, Name: Quality Assurance, Email: qa@pruebavana.com
Group Key: 02grqrue0tt2qub, Name: Human Resources, Email: rrhh@pruebavana.com
Group Key: 01gf8i834htmd9d, Name: Sales Group, Email: sales_group@pruebavana.com
Group Key: 03vac5uf412nefh, Name: Group Test, Email: test@pruebavana.com
```
### List all members of a group
1. In order to consult the members of a group, it is necessary to execute the script with the python3 environment variable followed by the name of the script. After executing the script, all the groups in the directory will be listed with their name and email, to perform the query. For members of a group, it is necessary to enter the email address of the group you wish to consult.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 list_groupAlias.py 
Groups Keys in the directory:
*Name: Accounting group, Email Group: accounting@pruebavana.com
*Name: Developers Gruop, Email Group: dev@pruebavana.com
*Name: Quality Assurance, Email Group: qa@pruebavana.com
*Name: Human Resources, Email Group: rrhh@pruebavana.com
*Name: Sales Group, Email Group: sales_group@pruebavana.com
*Name: Group Test, Email Group: test@pruebavana.com
Enter the group to be queried:
```
2. Once you have entered the email address of the group you wish to consult, a list of the members of said group will be displayed.
```
PruebaTecnica_VanaGoogleWorkspace$ python3 list_groupAlias.py 
Groups Keys in the directory:
*Name: Accounting group, Email Group: accounting@pruebavana.com
*Name: Developers Gruop, Email Group: dev@pruebavana.com
*Name: Quality Assurance, Email Group: qa@pruebavana.com
*Name: Human Resources, Email Group: rrhh@pruebavana.com
*Name: Sales Group, Email Group: sales_group@pruebavana.com
*Name: Group Test, Email Group: test@pruebavana.com
Enter the group to be queried:test@pruebavana.com
Members of the group test@pruebavana.com:
* Email: usertest@pruebavana.com
```
The configuration made to the Google project is designed for the scalability of future functions of this tool.
