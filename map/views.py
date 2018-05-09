# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from django.http import HttpResponse, JsonResponse
from serializers import *
from django.db.models import Q
from operator import __or__ as OR
# Create your views here.

def index (request):
    return render(request, 'map/index.html')
def ward_data(request):
    lst = [Q(scounty_id=36409),Q(scounty_id=36410),Q(scounty_id=36411),Q(scounty_id=36412)]
    ward = Ward.objects.select_related('scounty').filter(reduce(OR, lst))
    serializer = WardSerializer(ward, many=True)
    return JsonResponse(serializer.data)
def country_data(request):
    country = Country.objects.filter(id=1)
    serializer = CountrySerializer(country, many=True)
    return JsonResponse(serializer.data)

def county_data(request):
    county = County.objects.filter(id=18985)
    serializer = CountySerializer(county,many=True)
    return JsonResponse(serializer.data)
def scounty_data(request):
    scounty= Scounty.objects.select_related('county').filter(county_id=18985)
    serializer = ScountySerializer(scounty,many=True)
    return JsonResponse(serializer.data)
def business_data(request):
    business= Business.objects.all()
    serializer = BusinessSerializer(business, many=True)
    return JsonResponse(serializer.data)
def amenity_data(request):
    amenity= CommunityAmmenity.objects.all()
    serializer = CommunityAmmenitySerializer(amenity, many=True)
    return JsonResponse(serializer.data)
def incident_data(request):
    incident= Incident.objects.all()
    serializer = IncidentSerializer(incident, many=True)
    return JsonResponse(serializer.data)