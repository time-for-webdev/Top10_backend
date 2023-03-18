from django.urls import path
from vpn.views import home
urlpatterns = [
    path('',home,name ='home'),
]
