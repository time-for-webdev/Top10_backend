from rest_framework import serializers
from vpn.models import Top_ten,VpnList,All_avilable_filter,Form

class Top_Ten_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Top_ten
        fields = '__all__'


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