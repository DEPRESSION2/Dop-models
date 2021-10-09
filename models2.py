from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _


class Author(models.Model):
    pseudonym = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    NOT_SELECTED = 1
    COMEDY = 2
    ACTION = 3
    BEAUTY = 4
    OTHER = 5
    GENRE_CHOICES = (
        (NOT_SELECTED, _("Not selected")),
        (COMEDY, _("Comedy")),
        (ACTION, _("Action")),
        (BEAUTY, _("Beauty")),
        (OTHER, _("Other"))
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        related_name='articles',
    )
    text = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=NOT_SELECTED)

    def __str__(self):
        return f'Author - {self.author.name}, genre - {self.genre}, id - {self.id}'


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(
        'myapp.Comment',
        null=True, blank=True,
        on_delete=models.DO_NOTHING,
        related_name='comments',
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.text} by {self.user.username}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'By user {self.user.username} to article {self.article.id}'