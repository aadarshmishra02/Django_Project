from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default User model
admin.site.unregister(User)

# Register it again with your customizations (if any)
admin.site.register(User, UserAdmin)
