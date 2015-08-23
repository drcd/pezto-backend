from django.http import Http404, \
    HttpResponse, HttpResponseRedirect, \
    JsonResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden

from pastes.models import Paste

from django.contrib.auth import hashers
from django.views.decorators.csrf import csrf_exempt


# This entire thing is a documentation-nightmare. Comments will be added soon.

def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def get_paste(request, paste_id):
    if request.method == 'GET':
        try:
            paste = Paste.objects.get(id=paste_id)

            json = {
                'uid': paste.uid,
                'title': paste.title,
                'created_at': paste.created_at,
                'content': paste.content,
            }

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

    elif request.method == 'PUT':

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
            paste = Paste.objects.get(id=paste_id)

            if paste.password is None:
                err = {'error': 'This paste cannot be modified'}
                return JsonResponse(err, status=405)
            
            if (request.PUT.get('password') is None or
             request.PUT.get('password') == ""):
                err = {'error': 'Password needed to modify paste'}
                return JsonResponse(err, status=401)

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
                    'location': '/paste/%s' % paste.id,
                }
                response = JsonResponse(msg, status=200)
                response['Location'] = '/paste/%s' % paste.id
                return response
            else:
                err = {'error': 'Incorrect password'}
                return JsonResponse(err, status=401)

        except Paste.DoesNotExist:
            err = {'error': 'The requested paste does not exist'}
            return JsonResponse(err, status=404)

    elif request.method == 'DELETE':

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
            paste = Paste.objects.get(id=paste_id)

            if paste.password is None:
                err = {'error': 'This paste cannot be deleted'}
                return JsonResponse(err, status=405)
            
            if (request.DELETE.get('password') is None or
            request.DELETE.get('password') == ""):
                err = {'error': 'Password needed to delete paste'}
                return JsonResponse(err, status=401)

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

    else:
        err = {'error': 'Bad Request'}
        return JsonResponse(err, status=400)

@csrf_exempt
def get_paste_raw(request, paste_id):
    if request.method == 'GET':
        try:
            paste = Paste.objects.get(id=paste_id)
            text = paste.content

            return HttpResponse(text, status=200, content_type='text/plain')

        except Paste.DoesNotExist:
            err = 'Error: The requested paste does not exist'
            return HttpResponse(err, status=404, content_type='text/plain')
    else:
        err = 'Error: Bad Request'
        return HttpResponse(err, status=400, content_type='text/plain')

@csrf_exempt
def post_paste(request):
    if request.method == 'POST':
        if request.POST.get('content') is None:
            err = {'error': 'Paste content cannot be empty'}
            return JsonResponse(err, status=422)

        paste = Paste()
        paste.content = request.POST.get('content')

        if request.POST.get('title') is not None:
            paste.title = request.POST.get('title')

        if request.POST.get('password') is not None:
            paste.password = hashers.make_password(request.POST.get('password'))

        paste.ip_addr = _get_client_ip(request)

        paste.save()

        return HttpResponseRedirect('/paste/%s' % paste.id)
    else:
        err = {'error': 'Bad Request'}
        return JsonResponse(err, status=400)
