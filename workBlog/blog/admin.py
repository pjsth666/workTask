from django.contrib import admin
from .models import WorkBlog, HomeBlog
# Register your models here.
admin.site.register(WorkBlog)
admin.site.register(HomeBlog)
