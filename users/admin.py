from django.contrib import admin
# Register your models here.
from users.models import User, Group, UserGroup

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)