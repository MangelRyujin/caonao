from django.urls import path
from apps.educacion.views.educacion_views import educacion_view


urlpatterns = [
    path('educacion/',educacion_view,name='educacion_view'),
]