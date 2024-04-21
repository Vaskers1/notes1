from django import template
from notes_main.models import Notes, User

register = template.Library()


@register.simple_tag()
def get_notes():
    return Notes.objects.all()


@register.simple_tag()
def get_user():
    return User.objects.all()
