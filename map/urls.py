from django.conf.urls import url,include
from .views import *
app_name = 'map'
urlpatterns = [
    url(r'^$', index, name='map'),
    url(r'^ward.geojson$', ward_data, name='ward_data'),
    url(r'^country.geojson$', country_data, name='country_data'),
    url(r'^county.geojson$', county_data, name='county_data'),
    url(r'^scounty.geojson$', scounty_data, name='scounty_data'),
    url(r'^business.geojson$', business_data, name='business_data'),
    url(r'^amenity.geojson$', amenity_data, name='amenity_data'),
    url(r'^incident.geojson$', incident_data, name='incident_data'),
]