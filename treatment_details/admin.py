from django.contrib import admin
from .models import Treatment

# Register your models here.

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'slug')

admin.site.register(Treatment)