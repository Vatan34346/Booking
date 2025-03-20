from django.urls import path
from .views import booking_list, delete_booking, update_booking, create_booking, booking_events, calendar_view

urlpatterns = [
    path('', booking_list, name='booking_list'),
    path('new/', create_booking, name='create_booking'),
    path('<int:booking_id>/edit/', update_booking, name='update_booking'),
    path('<int:booking_id>/delete/', delete_booking, name='delete_booking'),
    path('events/', booking_events, name='booking_events'),
    path('calendar/', calendar_view, name='calendar_view')
]
