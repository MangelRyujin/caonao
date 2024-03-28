from django.urls import path
from apps.educacion.views.education_views import education_detail_view, education_list_view


urlpatterns = [
    path('educacion/',education_list_view,name='education_list_view'),
    path('educacion/<int:pk>/', education_detail_view, name='education_detail_view'),
]