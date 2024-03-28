from django.urls import path
from apps.oficoda.views.office_views import oficoda_view,oficoda_service_detail_view


urlpatterns = [
    path('oficoda/',oficoda_view,name='oficoda_view'),
     path('oficoda/<int:pk>',oficoda_service_detail_view,name='oficoda_detail_view'),

]