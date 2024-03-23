from django.urls import path
from apps.UNE.views.une_views import une_view


urlpatterns = [
    path('une/',une_view,name='une_view'),
]