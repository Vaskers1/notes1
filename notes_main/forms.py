from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    completion_status_tag = forms.ChoiceField(choices=Notes.completion_status, label='Статус выполнения')
    importance_status_tag = forms.ChoiceField(choices=Notes.importance_status, label='Статус важности')

    class Meta:
        model = Notes
        fields = ['note_title', 'note_text', 'completion_status_tag', 'importance_status_tag']
