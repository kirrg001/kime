from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def home(request):    
    if request.user.is_authenticated():
        jsonStr = render_to_string('online.html', {'user': request.user})
        return render_to_response('layout.html', {'content': jsonStr}, RequestContext(request))
    jsonStr = render_to_string('offline.html')
    return render_to_response('layout.html', {'content': jsonStr}, RequestContext(request))

@csrf_exempt
def user_login(request):
    username = request.POST['username']
    password = request.POST['username'] 
        
    user = authenticate(username=username, password=password)  
    if user:
        login(request, user)
    return HttpResponseRedirect('/')

@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')