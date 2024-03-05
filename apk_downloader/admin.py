# This file is not required for basic functionality.
# Uncomment and modify if you want to enable admin panel access for APK management.

from django.contrib import admin
from .models import Apk

admin.site.register(Apk)
