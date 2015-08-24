# /paste
## 'POST'
Uploads a paste
### Parameters
- title
- content
- password (optional)
***
# /paste/<uid>
## 'GET'
Retrieve a specific paste by UID
## 'PUT'
Updates a specific paste by UID.
Only pastes with a password can be edited.
### Parameters
- title (optional)
- content (optional)
- password
## 'DELETE'
Deletes a specific paste by UID.
Only pastes with a password can be deleted.
### Parameters
- password
