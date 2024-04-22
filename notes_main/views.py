from django.shortcuts import render


# Create your views here.
from notes_main.models import Notes


def index(request):
    return render(request, '../templates/notes_main/base.html')




def personal_notes(request):
    # Логика для отображения личных заметок
    personal_notes = Notes.objects.filter
    return render(request, 'notes_main/personal_notes.html')


def group_notes(request):
    return render(request, 'notes_main/group_notes.html')