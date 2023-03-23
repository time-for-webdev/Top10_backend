from django.forms import ModelForm
from vpn.models import VpnList

class Vpn_Form(ModelForm):
    class Meta:
        model = VpnList
        fields = '__all__'
        