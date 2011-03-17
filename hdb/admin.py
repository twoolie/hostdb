from django.contrib import admin

from models import *

admin.site.register(DNSZone)
admin.site.register(DHCPScope)
admin.site.register(Host)

class AddressAdmin(admin.ModelAdmin):
	list_display = ['host', 'type', 'address', 'vlan', 'mac']
	list_filter = ['type', 'vlan']
	search_fields = ['host__hostname', 'address', 'mac']
	list_editable = ['address', 'vlan']

admin.site.register(Address, AddressAdmin)
admin.site.register(DHCPHost)
admin.site.register(DNSRecord)
admin.site.register(DHCPOption)

class DHCPValueAdmin(admin.ModelAdmin):
	list_display = ['scope', 'host', 'option', 'value']

admin.site.register(DHCPValue, DHCPValueAdmin)

