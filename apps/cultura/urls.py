from django.urls import path
from apps.cultura.views.cultura_views import culture_list_view,culture_detail_view

urlpatterns = [
    path('cultura/',culture_list_view,name='culture_list_view'),
    path('cultura/<int:pk>', culture_detail_view, name='culture_detail_view'),
]