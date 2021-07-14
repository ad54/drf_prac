from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Friend)
admin.site.register(models.Borrowed)
admin.site.register(models.Belonging)