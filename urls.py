

from django.urls import path, re_path

from .views import index, articles, article_uniq, archive, archive_uniq, users
from .views import users_num, phone_number, code

urlpatterns = [

    path('', index, name='index'),

    path('articles/', articles, name='articles'),

    path('article/<int:article_id>/archive/', archive_uniq, name='uniq_archive'),

    path('articles/<int:article_id>/', article_uniq, name='uniq_arcticle'),

    path('articles/<int:article_id>/<slug:name>/', article_uniq, name='article_name'),

    path('articles/archive/', archive, name='archive'),

    path('users/', users, name='users'),

    path('users/<int:user_number>/', users_num, name='users_num'),

    path('[0-9]{10}', phone_number, name='phone_number'),

    re_path('[0-9a-f]{4}[-][0-9a-f]{6}', code, name='code'),
]