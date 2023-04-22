from django.urls import path
from .view import Vpn_with_id,Instruction,Vpn_without_id,get_logo_url,Form_without_id,Specification_without_id,DeviceWithoutId,DeviceWithId,LocationWithId,LocationWithoutId,ServiceWithId,ServiceWithoutId,FAQ_without_id,OwnerContactDetails_without_id

urlpatterns =[
    path('',Instruction,name = "Instruction"),
    path('vpn/',Vpn_without_id,name = "Vpn_without_id"),
    path('vpn/<str:pk>/',Vpn_with_id,name = "vpn_with_id"),
    path('vpn/<str:pk>/logo/',get_logo_url,name = "get_logo_url"),
    path('device/',DeviceWithoutId,name = 'DeviceWithoutId'),
    path('device/<str:pk>/',DeviceWithId,name = 'DeviceWithId'),
    path('location/',LocationWithoutId,name = 'LocationWithoutId'),
    path('location/<str:pk>/',LocationWithId,name = 'LocationWithId'), 
    path('service/',ServiceWithoutId,name = 'servicenWithoutId'),
    path('service/<str:pk>/',ServiceWithId,name = 'LocationWithId'),       
    path('form/',Form_without_id,name="Form_without_id"),
    path('specification/',Specification_without_id,name="Specification_without_id"),
    path('faq/',FAQ_without_id,name = 'FAQ_without_id'),
    path('owner_contact/',OwnerContactDetails_without_id,name='OwnerContactDetails_without_id'),
    
]

