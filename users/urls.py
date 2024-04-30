from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('user-registration/', views.user_registration, name='user_registration'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.logout, name='user_logout'),
    path('group-creation/', views.create_group, name='group_creation'),
]