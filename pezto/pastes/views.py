from django.http import Http404, \
    HttpResponse, HttpResponseRedirect, \
    JsonResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden

from pastes.models import Paste

from django.contrib.auth import hashers
from django.views.decorators.csrf import csrf_exempt


def _get_client_ip(request):
    """ Helper function to retrieve IP address from a request.
    It is placed above here, so that it can be called from the views below.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def paste_route(request, paste_uid=None):
    """ Checks the request method, and calls the correct function for the job.
    If the request method is something other than GET, POST, PUT or DELETE, it 
    will return a HTTP 400 Bad Request error.
    """
    if request.method == 'GET':
        return _read_paste(request, paste_uid)  # Read
    elif request.method == 'POST':
        return _create_paste(request)  # Create
    elif request.method == 'PUT':
        return _update_paste(request, paste_uid)  # Update
    elif request.method == 'DELETE':
        return _delete_paste(request, paste_uid)  # Delete
    else:
        err = {'error': 'Bad Request'}
        return JsonResponse(err, status=400)


def get_paste_raw(request, paste_uid):
    """ HTTP GET: Returns the content of the paste as raw text (text/plain) """
    
    ct = 'text/plain'

    if request.method == 'GET':
        try:
            paste = Paste.objects.get(uid=paste_uid)
            text = paste.content

            return HttpResponse(text, status=200, content_type=ct)

        except Paste.DoesNotExist:
            err = 'Error: The requested paste does not exist'
            return HttpResponse(err, status=404, content_type=ct)
    else:
        err = 'Error: Bad Request'
        return HttpResponse(err, status=400, content_type=ct)


def _read_paste(request, paste_uid):
    """ HTTP GET: Returns the requested paste as JSON """
    try:
        paste = Paste.objects.get(uid=paste_uid)

        json = {
            'uid': paste.uid,
            'title': paste.title,
            'created_at': paste.created_at,
            'content': paste.content,
        }

        # If a paste is password protected, the owner is then
        # able to modify or delete the paste.
        if paste.password is not None:
            json['is_editable'] = True
            json['is_deletable'] = True
            json['password_protected'] = True
        else:
            json['is_editable'] = False
            json['is_deletable'] = False
            json['password_protected'] = False

        return JsonResponse(json, status=200)

    except Paste.DoesNotExist:
        err = {'error': 'The requested paste does not exist'}
        return JsonResponse(err, status=404)


def _create_paste(request):
    """ HTTP POST: Creates a paste, and then returns the UID for the paste """
    if request.method == 'POST':
        if request.POST.get('content') is None:
            err = {'error': 'Paste content cannot be empty'}
            return JsonResponse(err, status=422)

        paste = Paste()
        paste.content = request.POST.get('content')

        # If a title is defined by the user, use the title provided.
        # Otherwise, it will fall back to "Untitled Paste"
        if request.POST.get('title') is not None:
            paste.title = request.POST.get('title')

        # If a password is provided, encrypt the password and then store
        if request.POST.get('password') is not None:
            paste.password = hashers.make_password(request.POST.get('password'))

        # Get the IP address from the request, using the helper function.
        paste.ip_addr = _get_client_ip(request)

        paste.save()

        msg = {
            'message': 'The paste has been successfully posted',
            'uid': paste.uid,
        }
        response = JsonResponse(msg, status=200)
        response['Location'] = str(paste.uid)  # Add Paste UID to Location header
        return response
    else:
        err = {'error': 'Bad Request'}
        return JsonResponse(err, status=400)


def _update_paste(request, paste_uid):
    """ HTTP PUT: Updates a paste, using a given password for confirmation.
    Only password-protected pastes can be modified.
    """
    # Hack to implement 'PUT' parameters
    # http://dada.theblogbowl.in/2014/12/how-to-use-requestput-or-requestdelete.html
    if hasattr(request, '_post'):
        del request._post
        del request._files
    try:
        request.method = "POST"
        request._load_post_and_files()
        request.method = "PUT"
    except AttributeError:
        request.META['REQUEST_METHOD'] = 'POST'
        request._load_post_and_files()
        request.META['REQUEST_METHOD'] = 'PUT'

    request.PUT = request.POST
    # End of hack
    try:
        paste = Paste.objects.get(uid=paste_uid)

        if paste.password is None:
            err = {'error': 'This paste cannot be modified'}
            return JsonResponse(err, status=405)
        
        if (request.PUT.get('password') is None or
        request.PUT.get('password') == ""):
            err = {'error': 'Password needed to modify paste'}
            return JsonResponse(err, status=401)

        # Check if the provided password matches
        _pw = request.PUT.get('password')
        _pw_check = hashers.check_password(_pw, paste.password)

        if _pw_check is True:
            # Set title (if any)
            if (request.PUT.get('title') is not None or
            request.PUT.get('title') == ""):
                paste.title = request.PUT.get('title')

            # Set content (if any)
            if (request.PUT.get('content') is not None or
            request.PUT.get('content') == ""):
                paste.content = request.PUT.get('content')

            # Save changes, and redirect
            paste.save()
            msg = {
                'message': 'The paste has been successfully modified',
                'uid': paste.uid,
            }
            response = JsonResponse(msg, status=200)
            response['Location'] = str(paste.uid)
            return response
        else:
            err = {'error': 'Incorrect password'}
            return JsonResponse(err, status=401)

    except Paste.DoesNotExist:
        err = {'error': 'The requested paste does not exist'}
        return JsonResponse(err, status=404)


def _delete_paste(request, paste_uid):
    """ HTTP DELETE: Deletes a paste, using a given password for confirmation.
    Only password-protected pastes can be deleted.
    """
    # Hack to implement 'DELETE' parameters
    # http://dada.theblogbowl.in/2014/12/how-to-use-requestput-or-requestdelete.html
    if hasattr(request, '_post'):
        del request._post
        del request._files
    try:
        request.method = "POST"
        request._load_post_and_files()
        request.method = "DELETE"
    except AttributeError:
        request.META['REQUEST_METHOD'] = 'POST'
        request._load_post_and_files()
        request.META['REQUEST_METHOD'] = 'DELETE'

    request.DELETE = request.POST
    # End of hack
    try:
        paste = Paste.objects.get(uid=paste_uid)

        if paste.password is None:
            err = {'error': 'This paste cannot be deleted'}
            return JsonResponse(err, status=405)
        
        if (request.DELETE.get('password') is None or
        request.DELETE.get('password') == ""):
            err = {'error': 'Password needed to delete paste'}
            return JsonResponse(err, status=401)

        # Check if the provided password matches
        _pw = request.DELETE.get('password')
        _pw_check = hashers.check_password(_pw, paste.password)

        if _pw_check is True:
            paste.delete()
            msg = {'message': 'The paste has been successfully deleted'}
            return JsonResponse(msg, status=200)
        else:
            err = {'error': 'Incorrect password'}
            return JsonResponse(err, status=401)

    except Paste.DoesNotExist:
        err = {'error': 'The requested paste does not exist'}
        return JsonResponse(err, status=404)

