from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home_details import views as home_views
from bookings import views as bookings_views

urlpatterns = [
    path('', include('home_details.urls')),
    path('subscribe/', home_views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('admin/', admin.site.urls),
    path('treatments/', include('treatment_details.urls')),
    path('accounts/', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
    path('booking_events/', bookings_views.booking_events, name='booking_events'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
