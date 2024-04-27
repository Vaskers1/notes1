from django import template

import users
from notes_main.models import Notes, User

register = template.Library()


@register.simple_tag()
def get_notes():
    return Notes.objects.all()


