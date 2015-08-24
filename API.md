## POST /paste
Uploads a paste
### Parameters
- title
- content
- password (optional)

## GET /paste/<uid>
Retrieve a specific paste by UID
### Parameters
None

## PUT /paste/<uid>
Updates a specific paste by UID.

Only pastes with a password can be edited.
### Parameters
- title (optional)
- content (optional)
- password

## DELETE /paste/<uid>
Deletes a specific paste by UID.

Only pastes with a password can be deleted.
### Parameters
- password
