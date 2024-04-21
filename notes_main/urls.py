from django.urls import path

from notes_main import views

app_name = 'notes_main'

urlpatterns = [
    path('', views.index, name='index')]
