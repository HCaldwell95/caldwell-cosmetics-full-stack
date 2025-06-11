from django.contrib import admin
from .models import Appointment
from .models import Booking

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')  
    list_filter = ('start_time', 'end_time')  
    search_fields = ('title',) 

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'treatment', 'get_date', 'get_time_slot', 'is_confirmed')
    list_filter = ('is_confirmed', 'treatment', 'appointment__start_time')  # filter by appointment start time
    search_fields = ('user__username', 'treatment')

    list_editable = ('is_confirmed',)

    def get_date(self, obj):
        # Assuming Appointment has a 'start_time' datetime field
        return obj.appointment.start_time.date() if obj.appointment else None
    get_date.admin_order_field = 'appointment__start_time'  # allows sorting by appointment start time
    get_date.short_description = 'Date'

    def get_time_slot(self, obj):
        # Return time part or any specific field for time slot from appointment
        return obj.appointment.start_time.time() if obj.appointment else None
    get_time_slot.admin_order_field = 'appointment__start_time'
    get_time_slot.short_description = 'Time Slot'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_view_permission(request, obj)

admin.site.register(Booking, BookingAdmin)
