from django import forms

from users.models import Group
from .models import Notes
from users.forms import GroupForm


class NoteForm(forms.ModelForm):
    completion_status_tag = forms.ChoiceField(choices=Notes.completion_status, label='Статус выполнения')
    importance_status_tag = forms.ChoiceField(choices=Notes.importance_status, label='Статус важности')

    class Meta:
        model = Notes
        fields = ['note_title', 'note_text', 'completion_status_tag', 'importance_status_tag', 'group']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.all()  # Устанавливаем queryset для поля group
