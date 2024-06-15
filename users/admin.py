from django.contrib import admin
# Register your models here.
from users.models import User, Group

admin.site.register(User)
admin.site.register(Group)


class UserLevelAdmin(admin.ModelAdmin):
    list_display = 'user_id'
