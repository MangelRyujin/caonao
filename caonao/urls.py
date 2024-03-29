"""
URL configuration for caonao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from caonao.views.service_views import service_view
from .views.home_views import home_view
from .views.fq_views import fq_view
from .views.about_us_views import about_us_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('appune/',include('apps.UNE.urls')),
    path('appsalud/',include('apps.salud.urls')),
    path('appoficoda/',include('apps.oficoda.urls')),
    path('appinstitution/',include('apps.institucion.urls')),
    path('appestado/',include('apps.estado.urls')),
    path('appeducacion/',include('apps.educacion.urls')),
    path('appcultura/',include('apps.cultura.urls')),
    path('appacueducto/',include('apps.acueducto.urls')),
    path('',home_view,name='home_view'),
    path('preguntas_frecuentes/',fq_view,name='fq_view'),
    path('sobre_nosotros/',about_us_view,name='about_us_view'),
    path('servicios/',service_view,name='service_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
