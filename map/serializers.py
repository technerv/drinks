from models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class CountrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Country
        geo_field = "geom"
        id_field = False
        fields = ('co_name', 'population','gadmid','iso','square_kil','populati_1')

class CountySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = County
        geo_field = "geom"
        id_field = False
        fields = ('code', 'c_name','capital')

class ScountySerializer(GeoFeatureModelSerializer):
    county = serializers.StringRelatedField()
    class Meta:
        model = Scounty
        geo_field = "geom"
        id_field = False
        fields = ('county', 'sc_name')

class LandUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUse
        fields = ('name', 'description')

class WardSerializer(GeoFeatureModelSerializer):
    scounty = serializers.StringRelatedField()
    class Meta:
        model = Ward
        geo_field = "geom"
        id_field = False
        fields = ('scounty', 'ward_name',)

class BusinessSerializer(GeoFeatureModelSerializer):
    land_use = serializers.StringRelatedField()
    business_type = serializers.StringRelatedField()
    class Meta:
        model = Business
        geo_field = "geom"
        id_field = False
        fields = ('name', 'land_use','business_type')
class CommunityAmmenitySerializer(GeoFeatureModelSerializer):
    community_ammenity_type = serializers.StringRelatedField()
    class Meta:
        model = CommunityAmmenity
        geo_field = "geom"
        id_field = False
        fields = ('name', 'community_ammenity_type')

class IncidentSerializer(GeoFeatureModelSerializer):
    incident_type = serializers.StringRelatedField()
    class Meta:
        model = Incident
        geo_field = "geom"
        id_field = False
        fields = ('number_of_people_involved', 'number_of_injuries','incident_type','description_of_incident','photo')