from rest_framework import serializers
from vpn.models import VpnList,Form,Specification,remark,Comparision,Device,Location,Service,FAQ,feature

class Comparision_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comparision
        fields = '__all__'


class Specification_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__' 


class feature_Serializer(serializers.ModelSerializer):
    class Meta:
        model = feature
        fields = '__all__'


class FAQSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = FAQ
        fields = '__all__'  


class remarks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = remark
        fields = '__all__'


class VpnList_Serializer(serializers.ModelSerializer):

    specification = Specification_Serializer(many = True)
    remark = remarks_Serializer()
    Comparision = Comparision_Serializer()
    feature = feature_Serializer(many = True)


    class Meta:
        model = VpnList
        fields = '__all__'    


class Form_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'       

class Device_Serializer(serializers.ModelSerializer):
    First = VpnList_Serializer()  
    Second = VpnList_Serializer()   
    Third = VpnList_Serializer()  
    Forth = VpnList_Serializer()  
    Fifth = VpnList_Serializer()  
    Sixth = VpnList_Serializer()  
    Seventh = VpnList_Serializer()   

    class Meta:
        model = Device
        fields = '__all__'      

class Location_Serializer(serializers.ModelSerializer):
    First = VpnList_Serializer()  
    Second = VpnList_Serializer()   
    Third = VpnList_Serializer()  
    Forth = VpnList_Serializer()  
    Fifth = VpnList_Serializer()  
    Sixth = VpnList_Serializer()  
    Seventh = VpnList_Serializer()   

    class Meta:
        model = Location
        fields = '__all__'    

class Service_Serializer(serializers.ModelSerializer):
    First = VpnList_Serializer()  
    Second = VpnList_Serializer()   
    Third = VpnList_Serializer()  
    Forth = VpnList_Serializer()  
    Fifth = VpnList_Serializer()  
    Sixth = VpnList_Serializer()  
    Seventh = VpnList_Serializer()   

    class Meta:
        model = Service
        fields = '__all__'     

                   


