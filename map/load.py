import sys,os
import csv
from django.contrib.gis.utils import LayerMapping
from .models import Country
from .models import County
from .models import Scounty
from .models import Ward, Business, CommunityAmmenity, CommunityAmmenityType, LandUse, BusinessType

from django.core.management import call_command
from StringIO import StringIO

out = StringIO()
county_mapping = {
    'code':       'code',
    'area':       'area',
    'perimeter':  'perimeter',
    'c_name':       'c_name',
    'shape_leng': 'shape_leng',
    'shape_area': 'shape_area',
    'pop_2009':   'pop_2009',
    'capital':    'capital',
    'id':         'id',
    'geom':       'MULTIPOLYGON',
}
county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/boundaries', 'County.shp'),
)




country_mapping = {
    'gadmid':     'gadmid',
    'iso':        'iso',
    'co_name':       'co_name',
    'population': 'population',
    'square_kil': 'square_kil',
    'populati_1': 'populati_1',
    'shapel_len': 'shapel_len',
    'shape_area': 'shape_area',
    'geom':       'MULTIPOLYGON',
}

country_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/boundaries', 'Country.shp'),
)
subcounty_mapping = {
    # 'county' : 'county_id',
    'county': {'id': 'county_id'},

    'id' : 'id',
    'sc_name' : 'sc_name',
    'shape_leng' : 'shape_leng',
    'shape_area' : 'shape_area',
    'geom' : 'MULTIPOLYGON',
}

subcounty_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/boundaries', 'subcounty.shp'),
)


ward_mapping = {
    'scounty': {'id': 'scounty_id'},
    'id':         'id',
    'ward_name':       'ward_name',
    'shape_leng': 'shape_leng',
    'shape_area': 'shape_area',
    'geom':       'MULTIPOLYGON',
}
ward_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/boundaries', 'newward.shp'),
)

business_mapping = {
    'land_use': {'id': 'lu_id'},
    'business_type': {'id': 'btype_id'},
    'name':       'name',
    'lat': 'lat',
    'long': 'long',
    'geom':    'POINT',
}
business_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/business', 'businesses.shp'),
)
amenity_mapping = {
    'community_ammenity_type': {'id': 'catype_id'},
    'name':       'name',
    'lat': 'lat',
    'long': 'long',
    'geom':    'POINT',
}
amenity_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/amenity', 'amenities.shp'),
)
def run(verbose=True):


    cm = LayerMapping(
        Country, country_shp, country_mapping,
        transform=False, encoding='iso-8859-1',
    )
    cm.save(strict=True, verbose=verbose)

    com = LayerMapping(
        County, county_shp, county_mapping,
        transform=False, encoding='iso-8859-1',
    )
    com.save(strict=True, verbose=verbose)

   dm = LayerMapping(
        Scounty, subcounty_shp, subcounty_mapping,
        transform=False, encoding='iso-8859-1',
    )
    dm.save(strict=True, verbose=verbose)

    lcm = LayerMapping(
        Ward, ward_shp, ward_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lcm.save(strict=True, verbose=verbose)


    call_command('loaddata', '/home/evanoskillz/pyprojects/drinks/map/data/json/amenitytype.json',
                 stdout=out)
    call_command('loaddata', '/home/evanoskillz/pyprojects/drinks/map/data/json/businesstype.json', stdout=out)
    call_command('loaddata', '/home/evanoskillz/pyprojects/drinks/map/data/json/landuse.json', stdout=out)

    businessmap = LayerMapping(
        Business, business_shp, business_mapping,
        transform=False, encoding='iso-8859-1',
    )
    businessmap.save(strict=True, verbose=verbose)

    amenitymap = LayerMapping(
        CommunityAmmenity, amenity_shp, amenity_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lcm.save(strict=True, verbose=verbose)
