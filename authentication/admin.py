from django.contrib import admin
from .models import User, UserProfile, UserDesignation

admin.site.register(UserProfile)
admin.site.register(UserDesignation)
