from django.urls import path

from notes_main import views

app_name = 'notes_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('personal-notes/', views.personal_notes, name='personal_notes'),
    path('group-notes/', views.group_notes, name='group_notes'),
]
