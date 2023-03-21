from rest_framework import serializers
from vpn.models import Top_ten,VpnList,All_avilable_filter,Form



class VpnList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = VpnList
        fields = '__all__'    


class All_available_filter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_avilable_filter
        fields = '__all__'   

class Form_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'         

class Top_Ten_Serializer(serializers.ModelSerializer):

    type =  All_available_filter_Serializer()
    First = VpnList_Serializer()  
    Second = VpnList_Serializer()   
    Third = VpnList_Serializer()  
    Forth = VpnList_Serializer()  
    Fifth = VpnList_Serializer()  
    Sixth = VpnList_Serializer()  
    Seventh = VpnList_Serializer()    
    Eighth = VpnList_Serializer()  
    Ninth = VpnList_Serializer()  
    Tenth = VpnList_Serializer()
    class Meta:
        model = Top_ten
        fields = '__all__'
