from django.contrib import admin

from .models import Trail
from .models import Comment

admin.site.register(Trail)
admin.site.register(Comment)
