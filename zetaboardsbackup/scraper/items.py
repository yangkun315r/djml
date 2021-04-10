from scrapy.contrib_exp.djangoitem import DjangoItem
from scrapy.item import Item, Field

from forum.models import Forum, Thread, Post, User, UserGroup


class ForumItem(DjangoItem):
    django_model = Forum


class ThreadItem(DjangoItem):
    django_model = Thread


class PostItem(DjangoItem):
    django_model = Post


class UserItem(DjangoItem):
    django_model = User


class UserGroupItem(DjangoItem):
    django_model = UserGroup
