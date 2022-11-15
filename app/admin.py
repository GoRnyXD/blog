from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'number', 'country', 'city')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'slug')

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'slug')

class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'created', 'published')
    list_display_links = ('id', 'user', 'slug')
    search_fields = ('id','title', 'user', 'slug')
    summernote_fields = ('text',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'post', 'created')
    list_display_links = ('id', 'user')
    search_fields = ('id','user', 'text')



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
