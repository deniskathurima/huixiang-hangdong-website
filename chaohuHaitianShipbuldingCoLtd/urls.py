"""
URL configuration for chaohuHaitianShipbuldingCoLtd project.

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
from django.urls import path
from . import views as chaohu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chaohu_views.home, name='home-url'),
    path('about1/', chaohu_views.about1, name='about1-url'),
    path('contact1/', chaohu_views.contact1, name='contact1-url'),
    path('shipBuilding/', chaohu_views.shipBuilding, name='shipBuilding-url'),
    path('seaHorse/', chaohu_views.seaHorse, name='seaHorse-url'),
    path('greenline1/', chaohu_views.greenLine1, name='greenline1-url'),
    path('finFin/', chaohu_views.finFin, name='finFin-url'),
    path('darEsSalaam/', chaohu_views.darEsSalaam, name='darEsSalaam-url'),
    path('barrackBarge/', chaohu_views.barrackBarge, name='barrackBarge-url'),
    path('10MDahor/', chaohu_views.mDahor, name='10MDahor-url'),
    path('10MPatrolBoat/', chaohu_views.mPatrolBoat, name='10MPatrolBoat-url'),
    path('dredging/', chaohu_views.dregering, name='dredging-url'),
    path('fishing/', chaohu_views.fishing, name='fishing-url'),
]
