from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, '../templates/notes_main/notes_main.html')
