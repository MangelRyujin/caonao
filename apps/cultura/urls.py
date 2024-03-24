from django.urls import path
from apps.cultura.views.cultura_views import cultura_list_view,cultura_detail_view

urlpatterns = [
    path('cultura/',cultura_list_view,name='cultura_list_view'),
    path('cultura/<int:pk>', cultura_detail_view, name='cultura_detail_view'),
]