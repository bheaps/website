from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import Report
from .models import Participant
from .models import Comment
from django.template import loader
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from forms import ReportsForm
from forms import ParticipantForm
from forms import CommentForm
from forms import ParticipantFormSet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

from haystack.query import SearchQuerySet

from datetime import datetime

def index(request):
    report_list=Report.objects.order_by('-date')
    paginator = Paginator(report_list,5)

    page=request.GET.get('page')
    try:
        reports=paginator.page(page)
    except PageNotAnInteger:
        reports=paginator.page(1)
    except EmptyPage:
        reports=paginator.page(paginator.num_pages)

    return render(request, 'reports/index.html', {'reports':reports})

def detail(request, report_id): #comment handling is here

    report=get_object_or_404(Report,pk=report_id)
    participants=Participant.objects.filter(report=report_id)
    comments=Comment.objects.filter(report=report_id)

    sess_comment=request.COOKIES.get("r"+str(report_id)+"comm",False)
    sess_like=request.COOKIES.get("r"+str(report_id)+"like",False)

    if request.POST:
        if sess_comment:
            return render(request,'reports/cantlike.html',{"report_id":report_id})#says you are only allowed to like/comment once
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()       
            
            response = render(request,'reports/commented.html',{'report_id':report_id})   
            response.set_cookie("r"+str(report_id)+"comm",True)
            return response

    form = CommentForm()
    form.fields["report"].initial=report

    return render(request,'reports/details.html',{'report':report,'participants':participants, 'form':form, 'comments':comments , 'combool':sess_comment, 'likbool':sess_like})


@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def create(request):
    if request.COOKIES.get("reports"):
        return render(request,'reports/cantcreatereport.html',[])
    if request.POST:
        form = ReportsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            response = HttpResponseRedirect('../addparticipants/')
            response.set_cookie("reports",True,max_age=3600)
            return response
    else:
        form = ReportsForm()

    form.fields["likes"].initial=0
    form.fields["dislikes"].initial=0
    form.fields["uname"].initial=request.user.username
    form.fields["writer"].initial=request.user.username

    args = {}
    

    args['form'] = form
    args['user']= request.user

    return render(request,'reports/create.html',args)

def dc(request):
    if request.COOKIES.get("reports"):
        response=HttpResponse("Cookie")
        response.delete_cookie("reports")
        return response
    else:
        return HttpResponse("No Cookie")
@csrf_protect
@login_required(redirect_field_name='/accounts/login/')
def addparticipants(request):
    if request.user.username != Report.objects.all().order_by('id')[0].uname:
        return HttpResponse("You are not supposed to be here")
    if request.POST:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../addparticipants')
    else:
        form = ParticipantForm()
    form.fields["report"].initial=Report.objects.all().order_by('-id')[0]
    args = {}


    args['form'] = form
    args['user'] = request.user
    participants=Participant.objects.filter(report=Report.objects.all().order_by('-id')[0])
    args['participants'] = participants
    return render(request,'reports/addparticipants.html',args)

def like(request, report_id):
    if request.COOKIES.get("r"+str(report_id)+"like"):
        return render(request,'reports/cantlike.html',{"report_id":report_id})
    report=get_object_or_404(Report,pk=report_id)
    report.likes=report.likes+1
    report.save()
    response = render(request,'reports/like.html',{"report_id":report_id})
    response.set_cookie("r"+str(report_id)+"like",True)
    return response

def dislike(request, report_id):
    if request.COOKIES.get("r"+str(report_id)+"like"):
        return render(request,'reports/cantlike.html',{"report_id":report_id})
    report=get_object_or_404(Report,pk=report_id)
    report.dislikes=report.dislikes+1
    report.save()
    response = render(request,'reports/like.html',{"report_id":report_id})
    response.set_cookie("r"+str(report_id)+"like",True)
    return response

@login_required(redirect_field_name='/accounts/login/')
def deleteparticipant(request, part_id):
    rep=Participant.objects.filter(pk=part_id)[0].report
    if rep.uname != request.user.username:
        return render(request, 'reports/cantmodify.html', {'report_id':rep.id})
        HttpResponse("You are not allowed to delete this participant")
    Participant.objects.filter(pk=part_id).delete()
    participants=Participant.objects.filter(report=Reports.objects.all().order_by('-id')[0])
    args={}
    args['participants'] = participants
    form = ParticipantForm()
    form.fields["report"].initial=Reports.objects.all().order_by('-id')[0]
    args['form'] = form
    return render(request,'reports/addparticipants.html',args)

#OLD SEARCHdef search(request):
    #if request.POST:
    #    search_text=request.POST['search']
    #    title_list=Reports.objects.filter(title__contains=search_text)
    #    text_list=Reports.objects.filter(text__contains=search_text)
    #    author_list=Reports.objects.filter(writer__contains=search_text)
    #    report_list=(title_list | text_list | author_list).order_by('-date')
        
    #if request.GET:
    #    search_text=request.GET.get('search')
    #    title_list=Reports.objects.filter(title__contains=search_text)
    #    text_list=Reports.objects.filter(text__contains=search_text)
    #    author_list=Reports.objects.filter(writer__contains=search_text)
    #    report_list=(title_list | text_list | author_list).order_by('-date')
    
    #paginator = Paginator(report_list,5)
    #page=request.GET.get('page')
    #try:
    #    reports=paginator.page(page)
    #except PageNotAnInteger:
    #    reports=paginator.page(1)
    #except EmptyPage:
    
    #if request.POST:
        #search_text=request.POST['search']
    #if request.GET:
        #search_text=request.GET.get('search')

    #reports=paginator.page(paginator.num_pages)

    #reports = SearchQuerySet().autocomplete(content_auto=search_text)

    #return render(request, 'reports/search.html', {'reports':reports,'search':search_text})
        
@csrf_protect    
@login_required(redirect_field_name='/accounts/login/')
def modify(request,report_id):
    if request.POST:
        report=get_object_or_404(Report,pk=report_id) #block in case hacker makes a POST
        if report.uname != request.user.username:
             return render(request, 'reports/cantmodify.html', {'report_id':report_id})
        form=ReportsForm(request.POST,request.FILES)
        if form.is_valid():
             
             report=get_object_or_404(Report,pk=report_id)

             report.text=form["text"].value()
             report.writer=form["writer"].value()
             report.title=form["title"].value()
             report.date=form["date"].value()
             report.trip_area=form["trip_area"].value()
             report.elevation_gain=form["elevation_gain"].value()
             report.distance_coverred=form["distance_coverred"].value()
             report.likes=form["likes"].value()
             report.dislikes=form["dislikes"].value()
             report.uname=form["uname"].value()

             
             report.save()

             return render(request,'reports/reportmodified.html',{"title":report.title, "id":report_id})
        
    else:
        
        report=get_object_or_404(Report,pk=report_id)
        if report.uname != request.user.username:
             return render(request, 'reports/cantmodify.html', {'report_id':report_id})
        form=ReportsForm(instance=report)
    args = {}


    args['form'] = form
    args['id'] = report_id
    args['user']=request.user

    return render(request,'reports/modify.html',args)#templates folder

@csrf_protect
@login_required(redirect_field_name='/accounts/login/')    
def modifyparticipants(request,report_id):

    report=get_object_or_404(Report,pk=report_id)
    if report.uname != request.user.username:
        return render(request, 'reports/cantmodify.html', {'report_id':report_id})
    if request.POST:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
        
            return HttpResponseRedirect('/reports/modifyparticipants/'+str(report_id)+'/')
    else:
        form = ParticipantForm()
    form.fields["report"].initial=get_object_or_404(Report,pk=report_id)
    args = {}


    args['form'] = form
    args['user'] = request.user
    participants=Participant.objects.filter(report=Report.objects.filter(pk=report_id))
    args['participants'] = participants
    args['id'] = report_id
    return render(request,'reports/modifyparticipants.html',args)#templates folder

@login_required(redirect_field_name='/accounts/login/')
def deleteparticipantmodify(request, part_id, report_id):

    report=get_object_or_404(Reports,pk=report_id)
    if report.uname != request.user.username:
        return render(request, 'reports/cantmodify.html', {'report_id':report_id})

    Participant.objects.filter(pk=part_id).delete()
    participants=Participant.objects.filter(report=Reports.objects.filter(pk=report_id))
    args={}
    args['participants'] = participants
    form = ParticipantForm()
    form.fields["report"].initial=report=get_object_or_404(Reports,pk=report_id)
    args['form'] = form
    args['id'] = report_id
    return render(request,'reports/modifyparticipants.html',args)#templates folder

#form with both database tables on one html page
def reportsparticipants(request):
    if request.POST:

        form = ReportsForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            participant_formset = ParticipantFormSet(request.POST, instance=report)
            if participant_formset.is_valid():
                report.save()
                participant_formset.save()
                return HttpResponseRedirect("/reports/")
    else:
        form = ReportsForm()
        participant_formset = ParticipantFormSet(instance=Reports())
    return render_to_response("reports/create2.html", {
        "form": form,
        "participant_formset": participant_formset,
    }, context_instance=RequestContext(request))

def reportadded(request):
    title=Report.objects.all().order_by('-id')[0].title
    return render(request,'reports/reportadded.html',{"title":title})

def commented(request,report_id):
    report_id=report_id
    return render(request,'reports/commented.html',{"report_id":report_id})

