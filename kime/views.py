from django.utils import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from models import Project, TimeEntry
import math
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

def logged_in(request):
    if request.user.is_authenticated():
        return True
    return False

def home(request):    
    if logged_in(request):
        user = request.user
        projects = Project.objects.filter(users__id=user.id)
        jsonStr = render_to_string('online.html', {'user': user, 'projects': projects})
    else:
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

def projects(request):
    
    l = 5
    
    if not logged_in(request):
        return HttpResponseRedirect('/')
    
    pi = request.GET.get('pi')
    os = int(request.GET.get('os'))
    
    limit = "%d:%d" % ((os * l), (os * l) + l)
    
    user = request.user
    time_entries = TimeEntry.objects.filter(project_id=pi).filter(user_id=user.id)
    time_entries = time_entries[::-1]
    
    projects = Project.objects.filter(users__id=user.id)    
    project = Project.objects.get(id=pi)
    
    number_of_entries = range(int(math.ceil((len(time_entries) / float(l)))))    
    
    jsonStr = render_to_string('time_entries.html', {'time_entries' : time_entries, 'os': os, 'limit': limit, 'pi': pi, 'number_of_entries': number_of_entries, 'users': project.users})
    jsonStr = render_to_string('online.html', {'time_entries' : jsonStr, 'projects': projects, 'user': user})
    return render_to_response('layout.html', {'content': jsonStr}, RequestContext(request))

@csrf_exempt
def save_time_entry(request):
    
    if not logged_in(request):
        return HttpResponseRedirect('/')
    
    st = request.POST.get('start_time')
    et = request.POST.get('end_time')
    day = request.POST.get('day')
    pi = request.POST.get('pi')
    ds = request.POST.get('description')
    user = request.user

    te = TimeEntry(user_id = user.id , start_time = st, end_time = et, day = day, project_id = pi, description=ds)
    te.save()
    return HttpResponse()
    
@csrf_exempt
def remove_time_entry(request):
    
    if not logged_in(request):
        return HttpResponseRedirect('/')
    
    id = request.POST.get('id')
    te = TimeEntry.objects.get(pk = id)
    te.delete()
    return HttpResponse()

@csrf_exempt
def update_time_entry(request):
    
    if not logged_in(request):
        return HttpResponseRedirect('/')
    
    st = request.POST.get('st')
    et = request.POST.get('et')
    id = request.POST.get('id')
    d = request.POST.get('d')
    des = request.POST.get('des')
        
    time_entry = TimeEntry.objects.get(pk = id)
    time_entry.start_time = st
    time_entry.end_time = et
    time_entry.description = des
    time_entry.day = d
    
    time_entry.save()
    return HttpResponse()