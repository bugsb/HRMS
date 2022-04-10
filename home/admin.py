from django.contrib import admin
from .models import *
# Register your models here.
my_models = [GM,RGM,AGM,DM]
admin.site.register(my_models)