from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')  
    list_filter = ('start_time', 'end_time')  
    search_fields = ('title',) 
