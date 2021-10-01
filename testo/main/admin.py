from django.contrib import admin
from .models import Task
from .models import Article, Comment

# Register your models here.
admin.site.register(Task)
admin.site.register(Article)
admin.site.register(Comment)

