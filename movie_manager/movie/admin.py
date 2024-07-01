from django.contrib import admin
from . models import movieinfo,Director,CensorInfo,Actor
# Register your models here.
admin.site.register(movieinfo)
admin.site.register(Director)
admin.site.register(CensorInfo)
admin.site.register(Actor)