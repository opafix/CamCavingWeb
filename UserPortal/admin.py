# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

admin.site.register(CustomUser)
admin.site.register(Rank)
admin.site.register(Committee)
