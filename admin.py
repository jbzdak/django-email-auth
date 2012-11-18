__author__ = 'jb'

from django.contrib import admin
from django.contrib.auth.models import User

import admin_hacks


UserModelAdmin = admin.site._registry[User]

UserModelAdmin.add_form = admin_hacks.UserAddForm
UserModelAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )