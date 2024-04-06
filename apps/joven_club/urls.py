from django.urls import path
from apps.joven_club.views.jc_views import joven_club_service_view

urlpatterns = [
    path('joven_club/',joven_club_service_view,name='joven_club_view'),
]