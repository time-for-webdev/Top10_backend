from django.urls import path
from vpn.views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import Form
urlpatterns = [
    path('',home,name ='home'),
    path('form/',Form,name="Form")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)