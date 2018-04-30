# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from models import *

# Register your models here.
admin.site.register(Country, admin.OSMGeoAdmin)
admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(Scounty, admin.OSMGeoAdmin)
admin.site.register(Ward, admin.OSMGeoAdmin)
admin.site.register(Business, admin.OSMGeoAdmin)
admin.site.register(CommunityAmmenity, admin.OSMGeoAdmin)
admin.site.register(BusinessType, admin.ModelAdmin)
admin.site.register(CommunityAmmenityType, admin.ModelAdmin)
admin.site.register(Incident, admin.OSMGeoAdmin)
admin.site.register(IncidentType, admin.ModelAdmin)
admin.site.register(LandUse, admin.ModelAdmin)

