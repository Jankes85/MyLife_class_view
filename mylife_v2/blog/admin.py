from django.contrib import admin

from . import models
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "note", "entry_date", "category")


admin.site.register(models.Blog, BlogAdmin)
