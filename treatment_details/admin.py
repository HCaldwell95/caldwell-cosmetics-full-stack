from django.contrib import admin
from .models import Treatment

# Register your models here.

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')

admin.site.register(Treatment)