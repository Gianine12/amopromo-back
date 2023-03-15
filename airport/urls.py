from django.urls import path
from .views import get_airpot, update_airport, activate_or_deactivate_airports, search_ticket_airline

urlpatterns = [
    path('', get_airpot),
    path('update/', update_airport),
    path('active_or_deactive/', activate_or_deactivate_airports),
    path('search_value/', search_ticket_airline)
]
