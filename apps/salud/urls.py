from django.urls import path
from apps.salud.views.salud_views import salud_view


urlpatterns = [
    path('salud/',salud_view,name='salud_view'),
]