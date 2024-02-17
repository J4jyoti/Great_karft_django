
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from Great_kart.settings import MEDIA_ROOT
from . import views
from store1.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('store1/',include('store1.urls')),
]+ static(settings.MEDIA_URL, document_root= MEDIA_ROOT )