from django.urls import path
from apps.salud.views.polyclinics_views import polyclinics_view,polyclinics_detail_view
from apps.salud.views.pharmacy_views import pharmacy_view,pharmacy_detail_view
from apps.salud.views.consultingRoom_views import consultingroom_view,consultingroom_detail_view
from apps.salud.views.salud_view import salud_view


urlpatterns = [
    path('salud/',salud_view,name='salud_view'),
    path('polyclinics/',polyclinics_view,name='polyclinics_view'),
    path('polyclinics/<int:pk>',polyclinics_detail_view,name='polyclinics_detail_view'),
    path('pharmacy/',pharmacy_view,name='pharmacy_view'),
    path('pharmacy/<int:pk>',pharmacy_detail_view,name='pharmacy_detail_view'),
    path('consultingroom/',consultingroom_view,name='consultingroom_view'),
    path('consultingroom/<int:pk>',consultingroom_detail_view,name='consultingroom_detail_view'),
]