from django.contrib import admin

# Register your models here.

from Chat.models import User
admin.site.register(User)