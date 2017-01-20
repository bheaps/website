from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import Imageotd
from .models import Comment
from django.template import loader
from django.views.decorators import csrf
from django.db import models
from forms import ImageotdForm
from forms import CommentForm
#from .models import ModelWithFileField
from PIL import Image



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required


def index(request):
    image_list=Imageotd.objects.all().order_by('-date')
    paginator = Paginator(image_list,4)

    page=request.GET.get('page')
    try:
        images=paginator.page(page)
    except PageNotAnInteger:
        images=paginator.page(1)
    except EmptyPage:
        images=paginator.page(paginator.num_pages)

    return render(request, 'imageotd/index.html', {'images':images})

def likeview(request):
    image_list=Imageotd.objects.all().order_by('-likdisdif')
    paginator = Paginator(image_list,4)

    page=request.GET.get('page')
    try:
        images=paginator.page(page)
    except PageNotAnInteger:
        images=paginator.page(1)
    except EmptyPage:
        images=paginator.page(paginator.num_pages)

    return render(request, 'imageotd/index.html', {'images':images})

def detail(request, pic_id): #comment handling is here

    image=get_object_or_404(Imageotd,pk=pic_id)
    comments=Comment.objects.filter(imageotd=pic_id)

    sess_comment=request.session.get("i"+str(pic_id)+"comm",False)
    sess_like=request.session.get("i"+str(pic_id)+"like",False)

    if request.POST:
        if sess_comment:
            return render(request,'imageotd/cantlike.html',{"pic_id":pic_id}) #says only allowed to like/dislike and comment once
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()       
            request.session["i"+str(pic_id)+"comm"] = True  
            return render(request,'imageotd/commented.html',{'pic_id':pic_id})   
    
    form = CommentForm()
    form.fields["imageotd"].initial=image

    return render(request,'imageotd/details.html',{'image':image,'comments':comments,'form':form, 'combool':sess_comment, 'likbool':sess_like})

@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def create(request):
    if request.POST:
        form = ImageotdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return render_to_response('imageotd/imageadded.html',{})
    else:
        form = ImageotdForm()

    form.fields["likes"].initial=0
    form.fields["dislikes"].initial=0
    form.fields["likdisdif"].initial=0
    form.fields["uname"].initial=request.user.username
    args = {}


    args['form'] = form
    args['user']= request.user

    return render(request,'imageotd/create.html',args)

@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def modify(request,pic_id):
    if request.POST:
        image=get_object_or_404(Imageotd,pk=pic_id)
        
#block in case hacker makes a POST
        if image.uname != request.user.username:
             return render(request, 'imageotd/cantmodify.html', {'pic_id':pic_id})

        form = ImageotdForm(request.POST,request.FILES)  
        #form=ModelFormWithFileField(request.POST,request.FILES)        
        if form.is_valid(): 
             
             image=get_object_or_404(Imageotd,pk=pic_id)
             
             image.title=form["title"].value()
             image.image=form["image"].value()
             image.date=form["date"].value()
             image.uname=form["uname"].value()
             image.desc=form["desc"].value()
             image.likes=form["likes"].value()
             image.dislikes=form["dislikes"].value()
             image.likdisdif=form["likdisdif"].value()

             image.save()

             return render(request,'imageotd/modified.html',{"title":image.title, "id":pic_id})
        
    else:
        
        image=get_object_or_404(Imageotd,pk=pic_id)
        if image.uname != request.user.username:
             return render(request, 'imageotd/cantmodify.html', {'pic_id':pic_id})
        form=ImageotdForm(instance=image)
        
        
    args = {}

    args['form'] = form
    args['id'] = pic_id
    args['user']=request.user

    return render(request,'imageotd/modify.html',args)#templates folder

def like(request, pic_id):
    if request.session.get("i"+str(pic_id)+"like"):
        return render(request,'imageotd/cantlike.html',{"pic_id":pic_id})
    request.session["i"+str(pic_id)+"like"] = True 
    image=get_object_or_404(Imageotd,pk=pic_id)
    image.likes=image.likes+1
    image.likdisdif=image.likdisdif+1
    image.save()
    return render(request,'imageotd/like.html',{"pic_id":pic_id})

def dislike(request, pic_id):
    if request.session.get("i"+str(pic_id)+"like"):
        return render(request,'imageotd/cantlike.html',{"pic_id":pic_id})
    request.session["i"+str(pic_id)+"like"] = True 
    image=get_object_or_404(Imageotd,pk=pic_id)
    image.dislikes=image.dislikes+1
    image.likdisdif=image.likdisdif-1
    image.save()
    return render(request,'imageotd/like.html',{"pic_id":pic_id})

