from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body']
    list_filter = ['id', 'title']

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'post_id']
    list_filter = ['user_id', 'post_id']

# @admin.register(CategoryPost)
# class CategoryPostAdmin(admin.ModelAdmin):
    # list_display = ['category', 'post_id']
    # list_filter = ['category_id', 'post_id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'id', 'body', 'created_time']
    list_filter = ['user_id', 'body', 'created_time']