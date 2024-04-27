
This document provides an overview of the backend API endpoints and data structures used in the application.

## Authentication

### Login
- URL: /auth/login
- Method: POST
- Payload: LoginPayload
- Authenticates a user by email and password.
- Example Request Body:
  {
    "email": "user@example.com",
    "password": "secretpassword"
  }

### Signup
- URL: /auth/signup
- Method: POST
- Payload: SignupPayload
- Registers a new user account.
- Example Request Body:
  {
    "email": "user@example.com",
    "password": "secretpassword",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Example Inc",
    "phone_number": "123-456-7890"
  }

## Files

### Upload File
- URL: /files/upload/
- Method: POST
- Authentication Required: Yes
- Uploads a file to the server.
- Example Request Body: (multipart form data)

### Delete File
- URL: /files/delete/{id}
- Method: DELETE
- Authentication Required: Yes
- Deletes a file by its ID.

### Rename File
- URL: /files/rename/{id}
- Method: POST
- Authentication Required: Yes
- Renames a file.
- Example Request Body:
  {
    "name": "new_filename.txt"
  }

### Move File
- URL: /files/move/{id}
- Method: POST
- Authentication Required: Yes
- Moves a file to another folder.
- Example Request Body:
  {
    "parent_id": "destination_folder_id"
  }

## Folders

### Create Folder
- URL: /folders/create/
- Method: POST
- Authentication Required: Yes
- Creates a new folder.
- Example Request Body:
  {
    "name": "New Folder",
    "parent_id": "parent_folder_id"
  }

### Delete Folder
- URL: /folders/delete/{id}
- Method: DELETE
- Authentication Required: Yes
- Deletes a folder by its ID.

### Rename Folder
- URL: /folders/rename/{id}
- Method: POST
- Authentication Required: Yes
- Renames a folder.
- Example Request Body:
  {
    "name": "New Folder Name"
  }

### Move Folder
- URL: /folders/move/{id}
- Method: POST
- Authentication Required: Yes
- Moves a folder to another location.
- Example Request Body:
  {
    "parent_id": "destination_parent_folder_id"
  }

### Get Children
- URL: /folders/folder/{id}
- Method: GET
- Authentication Required: Yes
- Retrieves the children of a folder.

## Workspaces

### Create Workspace
- URL: /workspaces/create/
- Method: POST
- Authentication Required: Yes
- Creates a new workspace.
- Example Request Body:
  {
    "name": "New Workspace",
    "owner_id": "user_id"
  }

### Delete Workspace
- URL: /workspaces/delete/{id}
- Method: POST
- Authentication Required: Yes
- Deletes a workspace by its ID.

### Get Workspaces
- URL: /workspaces/me
- Method: GET
- Authentication Required: Yes
- Retrieves workspaces associated with the authenticated user.

### Join Workspace
- URL: /workspaces/join
- Method: POST
- Authentication Required: Yes
- Allows a user to join a workspace.
- Example Request Body:
  {
    "workspace_id": "workspace_to_join_id"
  }

### Leave Workspace
- URL: /workspaces/leave/{id}
- Method: POST
- Authentication Required: Yes
- Allows a user to leave a workspace.

## Data Structures

### LoginPayload 
Structure for login request payload.

### SignupPayload 
Structure for signup request payload.

### FolderPayload 
Structure for folder-related requests. 

### WorkspacePayload 
Structure for workspace-related requests. 

### RenamePayload 
Structure for renaming requests. 

### RolePayload 
Structure for role-related requests. 

### MovePayload 
Structure for move-related requests.

## Router Setup
The router setup defines the API routes and connects them to the appropriate controllers and middlewares.
