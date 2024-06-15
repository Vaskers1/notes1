from django import template
from django.contrib.auth import get_user_model

from users.models import Group

User = get_user_model()
register = template.Library()


@register.simple_tag()
def get_users():
    return User.objects.all()


@register.simple_tag()
def get_groups():
    return Group.objects.all()