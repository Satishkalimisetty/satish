from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(topics)

admin.site.register(webpage)

admin.site.register(accessrecords)