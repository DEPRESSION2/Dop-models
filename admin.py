from django.contrib import admin

from .models import Article, Author, Comment, Like

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)