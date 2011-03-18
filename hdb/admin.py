from django.contrib import admin

from models import *

class DNSZoneAdmin(admin.ModelAdmin):
	search_fields = ['zonename']

admin.site.register(DNSZone, DNSZoneAdmin)

class DHCPScopeAdmin(admin.ModelAdmin):
	search_fields = ['zonename']

admin.site.register(DHCPScope, DHCPScopeAdmin)

class HostAdmin(admin.ModelAdmin):
	search_fields = ['zone__zonename', 'hostname', 'User__name', 'location']
	list_display = ['hostname', 'os', 'owner']

admin.site.register(Host, HostAdmin)

class AddressAdmin(admin.ModelAdmin):
	list_display = ['host', 'type', 'address', 'vlan', 'mac']
	list_filter = ['type', 'vlan']
	search_fields = ['host', 'address', 'mac']
	list_editable = ['address', 'vlan']

admin.site.register(Address, AddressAdmin)

class DHCPHostAdmin(admin.ModelAdmin):
	pass

admin.site.register(DHCPHost, DHCPHostAdmin)

class DNSRecordAdmin(admin.ModelAdmin):
	list_display = ['address', 'zone', 'type', 'record']

admin.site.register(DNSRecord, DNSRecordAdmin)

class DHCPOptionAdmin(admin.ModelAdmin):
	list_display = ['name', 'code']

admin.site.register(DHCPOption, DHCPOptionAdmin)

class DHCPValueAdmin(admin.ModelAdmin):
	list_display = ['scope', 'host', 'option', 'value']

admin.site.register(DHCPValue, DHCPValueAdmin)

