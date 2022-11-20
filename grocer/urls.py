from django.urls import path
from .views import *

urlpatterns = [
    path("",landingPage, name='landing_page' )
]