from django.contrib import admin
from .models import Sweet

@admin.register(Sweet)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
