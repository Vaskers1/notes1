from django.contrib import admin

# Register your models here.
from notes_main.models import User, Group, UserGroup, Notes

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Notes)