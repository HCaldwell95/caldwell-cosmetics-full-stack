from django.contrib import admin
from .models import Appointment
from .models import Booking

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')  
    list_filter = ('start_time', 'end_time')  
    search_fields = ('title',) 

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'treatment', 'date', 'time_slot', 'is_confirmed')
    list_filter = ('is_confirmed', 'date', 'treatment')
    search_fields = ('user__username', 'treatment')

    list_editable = ('is_confirmed',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all bookings
        return qs.filter(user=request.user)  # Regular users see only their bookings

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Users can only change their own bookings
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Users can only delete their own bookings
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Users can only view their own bookings
        return super().has_view_permission(request, obj)

admin.site.register(Booking, BookingAdmin)