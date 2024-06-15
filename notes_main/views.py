from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.functional import SimpleLazyObject

# Create your views here.
from notes_main.forms import NoteForm
from notes_main.models import Notes
from users.forms import GroupForm



def index(request):
    return render(request, '../templates/notes_main/base.html')


def personal_notes(request):
    # Логика для отображения личных заметок
    return render(request, 'notes_main/personal_notes.html')


def group_notes(request):
    return render(request, 'notes_main/group_notes.html')


@login_required
def note_creation(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note_title = form.cleaned_data['note_title']
            note_text = form.cleaned_data['note_text']
            completion_status_tag = form.cleaned_data['completion_status_tag']
            importance_status_tag = form.cleaned_data['importance_status_tag']
            user = request.user
            group = form.cleaned_data['group']
            note = Notes.objects.create(note_title=note_title, note_text=note_text,
                                        completion_status_tag=completion_status_tag,
                                        importance_status_tag=importance_status_tag,
                                        user=user, group=group)
            # Дополнительные действия, например, перенаправление на другую страницу
            return redirect('note-creation:note_creation')
    else:
        form = NoteForm()
    return render(request, 'notes_main/note_creation.html', {'form': form})



