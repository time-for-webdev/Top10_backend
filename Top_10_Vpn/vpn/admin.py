from django.contrib import admin
from vpn.models import VpnList,Device,Location,Service,Form,Specification,remark,Comparision,FAQ,feature,OwnerContactDetails
# Register your models here.

admin.site.register(VpnList)
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Form)
admin.site.register(Specification)
admin.site.register(remark)
admin.site.register(Comparision)
admin.site.register(FAQ)
admin.site.register(feature)
admin.site.register(OwnerContactDetails)






