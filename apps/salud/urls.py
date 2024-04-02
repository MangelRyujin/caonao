from django.urls import path
from apps.salud.views.polyclinics_views import polyclinics_view,polyclinics_detail_view


urlpatterns = [
    path('polyclinics/',polyclinics_view,name='polyclinics_view'),
    path('polyclinics/<int:pk>',polyclinics_detail_view,name='polyclinics_detail_view')
]