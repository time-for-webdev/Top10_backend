from django.contrib import admin
from vpn.models import VpnList,All_avilable_filter,Top_ten,Device,Location,Service,Form
# Register your models here.

admin.site.register(VpnList)
admin.site.register(All_avilable_filter)
admin.site.register(Top_ten)
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Form)






