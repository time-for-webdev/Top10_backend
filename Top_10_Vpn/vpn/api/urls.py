from django.urls import path
from .view import Top_10_without_id,Top_10_with_id,Vpn_with_id,Instruction,Vpn_without_id,All_avilable_filter_with_id,All_avilable_filter_without_id,get_logo_url,Form_without_id,Specification_without_id
urlpatterns =[
    path('',Instruction,name = "Instruction"),
    path('vpn/',Vpn_without_id,name = "Vpn_without_id"),
    path('vpn/<str:pk>/',Vpn_with_id,name = "vpn_with_id"),
    path('vpn/<str:pk>/logo/',get_logo_url,name = "get_logo_url"),
    path('All_available_filter',All_avilable_filter_without_id,name="All_avilable_filter_without_id"),
    path('All_available_filter/<str:pk>/',All_avilable_filter_with_id,name="All_avilable_filter_with_id"),
    path('Top_ten/', Top_10_without_id,name=" Top_10_without_id"),
    path('Top_ten/<str:pk>/',Top_10_with_id,name="Top_10_with_id"),
    path('form/',Form_without_id,name="Form_without_id"),
    path('specification/',Specification_without_id,name="Specification_without_id"),
    
]