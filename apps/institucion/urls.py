from django.urls import path
from apps.institucion.views.instituciones_view import institucion_view


urlpatterns = [
    path('instuticion/',institucion_view,name='institucion_view'),
]