from django.urls import path
from apps.cultura.views.cultura_views import cultura_view

urlpatterns = [
    path('cultura/',cultura_view,name='cultura_view'),
]