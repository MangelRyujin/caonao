from django.urls import path
from apps.acueducto.views.acueducto_views import acueducto_view


urlpatterns = [
    path('acueducto/',acueducto_view,name='acueducto_view'),
]