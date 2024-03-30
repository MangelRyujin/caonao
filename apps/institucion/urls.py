from django.urls import path
from apps.institucion.views.institutions_views import institution_view,institutions_detail_view,institutions_type_view


urlpatterns = [
    path('institution/',institution_view,name='institution_view'),
    path('institution/<int:pk>', institutions_detail_view, name='institution_detail_view'),
    path('institution/<str:type>', institutions_type_view, name='institutions_type_view'),
]