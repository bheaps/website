from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Trail, Comment
from django.template import loader
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from forms import TrailForm, CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

def index(request):
    trail_list=Trail.objects.all().order_by("title")
    paginator = Paginator(trail_list,20)

    page=request.GET.get('page')
    try:
        trails=paginator.page(page)
    except PageNotAnInteger:
        trails=paginator.page(1)
    except EmptyPage:
        trails=paginator.page(paginator.num_pages)

    return render(request, 'trails/index.html', {'trails':trails})


def detail(request, trail_id):
    trail=get_object_or_404(Trail,pk=trail_id)
    comments=Comment.objects.filter(trail=trail_id)

    sess_comment=request.COOKIES.get("t"+str(trail_id)+"comm",False)
    sess_like=request.COOKIES.get("t"+str(trail_id)+"like",False)

    if request.POST:
        if sess_comment:
            return render(request,'trails/cantlike.html',{"trail_id":trail_id})
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()    
             
            response = render(request,'trails/commented.html',{'trail_id':trail_id})    
            response.set_cookie("t"+str(trail_id)+"comm",True)   
            return response  
    
    form = CommentForm()
    form.fields["trail"].initial=trail

    return render(request,'trails/details.html',{'trail':trail, 'form':form, 'comments':comments, 'combool':sess_comment, 'likbool':sess_like})

@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def create(request):
    if request.COOKIES.get("trails"):
        return render(request,'trails/cantcreatetrail.html',[])
    if request.POST:
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title=Trail.objects.all().order_by('-id')[0].title
            response = render_to_response('trails/trailcreated.html',{"title":title})
            response.set_cookie("trails",True,max_age=3600)
            return response
    else:
        form = TrailForm()

    form.fields["likes"].initial=0
    form.fields["dislikes"].initial=0
    form.fields["uname"].initial=request.user.username
    form.fields["writer"].initial=request.user.username
    args = {}
   

    args['user'] = request.user
    args['form'] = form

    return render(request,'trails/create.html',args)

def dc(request):
    if request.COOKIES.get("trails"):
        response=HttpResponse("Cookie")
        response.delete_cookie("trails")
        return response
    else:
        return HttpResponse("No Cookie")

def like(request, trail_id):
    if request.COOKIES.get("t"+str(trail_id)+"like"):
        return render(request,'trails/cantlike.html',{"trail_id":trail_id})
    trail=get_object_or_404(Trail,pk=trail_id)
    trail.likes=trail.likes+1
    trail.save()
    response = render(request,'trails/like.html',{"trail_id":trail_id})
    response.set_cookie("t"+str(trail_id)+"like",True)
    return response

def dislike(request, trail_id):
    if request.session.get("t"+str(trail_id)+"like"):
        return render(request,'trails/cantlike.html',{"trail_id":trail_id})
    trail=get_object_or_404(Trail,pk=trail_id)
    trail.dislikes=trail.dislikes+1
    trail.save()
    response = render(request,'trails/like.html',{"trail_id":trail_id})
    response.set_cookie("t"+str(trail_id)+"like",True)
    return reponse

#old searchdef search(request):
    #if request.POST:
        #search_text=request.POST['search']
        #trail_list=Trail.objects.filter(title__contains=search_text) | Trail.objects.filter(details__contains=search_text)

    #if request.GET:
        #search_text=request.GET.get('search')
        #trail_list=Trail.objects.filter(title__contains=search_text) | Trail.objects.filter(details__contains=search_text)

    #paginator = Paginator(trail_list,2)
    #page=request.GET.get('page')
    #try:
        #trails=paginator.page(page)
    #except PageNotAnInteger:
        #trails=paginator.page(1)
    #except EmptyPage:
        #trails=paginator.page(paginator.num_pages)

    #return render(request, 'trails/search.html', {'trails':trails,'search':search_text})

@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def modify(request,trail_id):
    if request.POST:
        trail=get_object_or_404(Trail,pk=trail_id) #block in case hacker makes a POST
        if trail.uname != request.user.username:
             return render(request, 'trails/cantmodify.html', {'report_id':report_id})
        
        form=TrailForm(request.POST, request.FILES)
        if form.is_valid():

             trail=get_object_or_404(Trail,pk=trail_id)

             trail.directions=form["directions"].value()
             trail.details=form["details"].value()
             trail.writer=form["writer"].value()
             trail.title=form["title"].value()
             trail.time=form["time"].value()
             trail.activity=form["activity"].value()
             trail.trip_area=form["trip_area"].value()
             trail.season=form["season"].value()
             trail.elevation_gain=form["elevation_gain"].value()
             trail.distance_coverred=form["distance_coverred"].value()
             trail.likes=form["likes"].value()
             trail.dislikes=form["dislikes"].value()
             trail.uname=form["uname"].value()
             trail.image=form["image"].value()
             trail.save()

             return render(request,'trails/trailmodified.html',{"title": trail.title, "id":trail_id})
    else:
        trail=get_object_or_404(Trail,pk=trail_id)
        if trail.uname != request.user.username:
             return render(request, 'trails/cantmodify.html', {'trail_id':trail_id})
        form=TrailForm(instance=trail)

    args = {}


    args['form'] = form
    args['id'] = trail_id
    args['user']=request.user

    return render(request,'trails/modify.html',args)#templates folder
