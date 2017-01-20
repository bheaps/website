from __future__ import unicode_literals

from time import time
from django.utils import timezone as django_tz 

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

def get_upload_file_name(instance, filename): #errors when I remove even though its not used 
    return "report_images/"+filename

class Report(models.Model):
    def __str__(self):
        return self.title

    text=RichTextUploadingField() #models.TextField()
    writer=models.CharField(max_length=70,blank=True)
    title=models.CharField(max_length=70)

    date=models.DateField(default=django_tz.now(),blank=True)
    trip_area=models.CharField(max_length=70,blank=True)
    elevation_gain=models.CharField(max_length=70,blank=True)
    distance_coverred=models.CharField(max_length=70,blank=True)
    likes = models.IntegerField(default=0,blank=True)
    dislikes = models.IntegerField(default=0,blank=True)
    uname = models.CharField(max_length=30,blank=True)
 
    def get_absolute_url(self):
        return "../reports/%i" % self.id

class Participant(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=50)
    report=models.ForeignKey(Report)

class Comment(models.Model):
    def __str__(self):
        return self.content

    content=models.TextField()
    report=models.ForeignKey(Report)

def get_absolute_url(self):
    return "/reports/%i/" % self.id
    

