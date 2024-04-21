from django import template
from notes_main.models import Notes, User

register = template.Library()


@register.simple_tag()
def get_notes():
    return Notes.objects.all()


@register.simple_tag()
def get_note_author(note_id):
    note = Notes.objects.get(id=note_id)
    return note.nickname

