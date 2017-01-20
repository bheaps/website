from __future__ import unicode_literals

from django.db import models

class Trail(models.Model):
    def __str__(self):
        return self.title

    writer=models.CharField(max_length=200,blank=True)
    title=models.CharField(max_length=200)
    directions=models.TextField()
    details=models.TextField()

    time=models.CharField(max_length=200)
    activity=models.CharField(max_length=200,blank=True)
    season=models.CharField(max_length=200,blank=True)
    trip_area=models.CharField(max_length=200,blank=True)
    elevation_gain=models.CharField(max_length=200)
    distance_coverred=models.CharField(max_length=200)
    likes = models.IntegerField(default=0,blank=True)
    dislikes = models.IntegerField(default=0,blank=True)
    uname = models.CharField(max_length=20, blank=True)
    image = models.FileField(upload_to='trails/%Y/%m/%d',blank=True)
    
    def get_absolute_url(self):
        return "../trails/%i" % self.id

class Comment(models.Model):
    def __str__(self):
        return self.content

    content=models.TextField()
    trail=models.ForeignKey(Trail)

