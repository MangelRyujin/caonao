from django.urls import path
from apps.institucion.views.bodega_views import bodega_view,bodega_detail_view


urlpatterns = [
    path('institution/',bodega_view,name='institution_view'),
    path('institution/<int:pk>', bodega_detail_view, name='institution_detail_view'),
]