from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.template import loader
from django.views.decorators import csrf

from django.contrib import auth
from forms import MyRegistrationForm
from imageotd.models import Imageotd
#from .forms import ModelFormWithFileField
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from reports.models import Report

def index(request):
    front_image=Imageotd.objects.all().order_by('-date')[0]
    
    template=loader.get_template('base.html')
    context = {}
    context["image"]= front_image

    report_list=Report.objects.order_by('-date')[:5]
    context["reports"]=report_list

    return HttpResponse(template.render(context,request))

@csrf_protect
def login(request):    
    if request.session.get("uli"): #user logged in 
        return render_to_response('loggedin.html', { 'full_name': request.user.username,'user':request.user})
    c = {}
    
    c["user"] = request.user
    return render(request,'login.html', c)

@csrf_protect
def auth_view(request):
    username= request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session["uli"]=request.user.username

        return HttpResponseRedirect('/accounts/loggedin')

    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', { 'full_name': request.user.username,'user':request.user})

@csrf_protect
def invalid_login(request):
    if request.session.get("uli"):
        return render_to_response('loggedin.html', { 'full_name': request.user.username,'user':request.user})
    return render(request,'invalid_login.html', {'user':request.user})

@csrf_protect
def logout(request):
    auth.logout(request)
    if request.session.get("uli"):
        del request.session["uli"]
    return render(request,'loggedout.html',{'user':request.user})

@csrf_protect
def register_user(request):
    args = {}
    
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = MyRegistrationForm()


    args['form'] = form
    args['user'] = request.user

    return render(request,'register.html', args)

def register_success(request):
    return render_to_response('register_success.html',{'user':request.user})


