from django import template


from notes_main.models import Notes

register = template.Library()


@register.simple_tag()
def get_notes():
    return Notes.objects.all()


