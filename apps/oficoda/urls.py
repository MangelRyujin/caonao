from django.urls import path
from apps.oficoda.views.office_views import oficoda_view


urlpatterns = [
    path('oficoda/',oficoda_view,name='oficoda_view'),
]