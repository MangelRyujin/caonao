from django.urls import path
from apps.acueducto.views.waterPlanning_views import waterPlanning_view


urlpatterns = [
    path('acueducto/',waterPlanning_view,name='waterPlanning_view'),
]