from django.contrib import admin
from .models import blogPost,comments
# Register your models here.


@admin.register(blogPost)
class Admin(admin.ModelAdmin):
    list_display = ["title"]
    


@admin.register(comments)
class Admin(admin.ModelAdmin):
    list_display = ["name","ostan"]

