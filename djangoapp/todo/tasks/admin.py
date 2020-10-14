from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Task) # after migrating db, we need to see the Task model in the admin panel

