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

## GET /paste/<uid>/raw  or  GET /paste/<uid>.txt
Returns the content of the paste as plain text.

The latter one (/paste/<uid>.txt) is especially good for downloading.
### Parameters
None