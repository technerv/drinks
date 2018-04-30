# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models
from reversion import revisions as reversion
class Country(models.Model):
    gadmid = models.IntegerField()
    iso = models.CharField(max_length=5)
    co_name = models.CharField(max_length=50)
    population = models.FloatField()
    square_kil = models.FloatField()
    populati_1 = models.FloatField()
    shapel_len = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    slug=models.SlugField(unique=True, editable=False,max_length=255, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__ (self):
        return self.co_name

@receiver(pre_save, sender=Country)
def country_pre_save(signal, instance, sender, **kwargs):
        if not instance.slug:
            fresh_slug = "{slug}-{randstr}".format(
                slug=instance.co_name,
                randstr=util.random_string_generator(size=4),
                # id=instance.identification_code
            )
            slug = slugify(fresh_slug.lower())
            new_slug = slug
            count = 0
            while Country.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
                count += 1
                new_slug = "{slug}-{randstr}".format(
                slug=instance.co_name,
                randstr=util.random_string_generator(size=4),
                # id=instance.identification_code
            )
            instance.slug = new_slug.lower()
signals.pre_save.connect(country_pre_save, sender=Country)



reversion.register(Country)

class CountyManager(models.Manager):
    def get_by_natural_key(self, name,code):
        return self.get(name=name, code=code)


class County(models.Model):
    # objects = CountyManager()
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    c_name = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    pop_2009 = models.BigIntegerField()
    capital = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=255, allow_unicode=True)
    def __str__ (self):
        return self.c_name

    def natural_key(self):
        return (self.c_name,self.code)

# Auto-generated `LayerMapping` dictionary for County model
@receiver(pre_save, sender=County)
def county_pre_save(signal, instance, sender, **kwargs):
        if not instance.slug:
            fresh_slug = "{slug}-{randstr}".format(
                slug=instance.c_name,
                randstr=util.random_string_generator(size=4),
                # id=instance.identification_code
            )
            slug = slugify(fresh_slug.lower())
            new_slug = slug
            count = 0
            while County.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
                count += 1
                new_slug = "{slug}-{randstr}".format(
                slug=instance.c_name,
                randstr=util.random_string_generator(size=4),
                # id=instance.identification_code
            )
            instance.slug = new_slug.lower()
signals.pre_save.connect(county_pre_save, sender=County)


class ScountyManager(models.Manager):
    def get_by_natural_key(self, c_name):
        return self.get(c_name=c_name )


reversion.register(County)
class Scounty(models.Model):
    objects = ScountyManager()
    county = models.ForeignKey(County, on_delete=models.CASCADE,related_name='subcounties')
    id = models.IntegerField(primary_key=True)
    sc_name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=255, allow_unicode=True)
    def __str__ (self):
        return self.sc_name

    def natural_key(self):
        return (self.sc_name)
    # Auto-generated `LayerMapping` dictionary for SubCounty model

@receiver(pre_save, sender=Scounty)
def scounty_pre_save(signal, instance, sender, **kwargs):
        if not instance.slug:
            fresh_slug = "{slug}-{county}-{randstr}".format(
                slug=instance.sc_name,
                randstr=util.random_string_generator(size=4),
                county=instance.county.c_name
            )
            slug = slugify(fresh_slug.lower())
            new_slug = slug
            count = 0
            while Scounty.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
                count += 1
                new_slug = "{slug}-{county}-{randstr}".format(
                slug=instance.sc_name,
                randstr=util.random_string_generator(size=4),
                county=instance.county.c_name
            )
            instance.slug = new_slug.lower()
signals.pre_save.connect(scounty_pre_save, sender=Scounty)


reversion.register(Scounty)
class WardManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name )

class Ward(models.Model):
    objects = WardManager()
    scounty = models.ForeignKey(Scounty, on_delete=models.CASCADE,related_name='wards')
    id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=255, allow_unicode=True)

    def __str__ (self):
        return self.ward_name

    def natural_key(self):
        return (self.ward_name)

# Auto-generated `LayerMapping` dictionary for Ward model

@receiver(pre_save, sender=Ward)
def ward_pre_save(signal, instance, sender, **kwargs):
        if not instance.slug:
            fresh_slug = "{slug}-{scounty}-{randstr}".format(
                slug=instance.ward_name,
                randstr=util.random_string_generator(size=4),
                scounty=instance.scounty.sc_name
            )
            slug = slugify(fresh_slug.lower())
            new_slug = slug
            count = 0
            while Ward.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
                count += 1
                new_slug = "{slug}-{scounty}-{randstr}".format(
                slug=instance.ward_name,
                randstr=util.random_string_generator(size=4),
                scounty=instance.scounty.sc_name
            )
            instance.slug = new_slug.lower()
signals.pre_save.connect(ward_pre_save, sender=Ward)

class Business(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    lat = models.FloatField()
    long = models.FloatField()
    geom = models.PointField(srid=4326)
    land_use = models.ForeignKey('LandUse',on_delete=models.CASCADE, blank=True, null=True)
    business_type = models.ForeignKey('BusinessType',on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'business'

        def __str__(self):
            return self.name

class BusinessType(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'business_type'

        def __str__(self):
            return self.name

class CommunityAmmenity(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    community_ammenity_type = models.ForeignKey('CommunityAmmenityType',on_delete=models.CASCADE, blank=True, null=True)
    lat = models.FloatField()
    long = models.FloatField()
    geom = models.PointField(srid=4326)
    class Meta:
        db_table = 'community_ammenity'

        def __str__(self):
            return self.name

class CommunityAmmenityType(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'community_ammenity_type'

    def __str__(self):
        return self.name


class Incident(models.Model):
    number_of_people_involved = models.CharField(max_length=45, blank=True, null=True)
    number_of_injuries = models.CharField(max_length=45, blank=True, null=True)
    incident_type = models.ForeignKey('IncidentType',on_delete=models.CASCADE, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    long = models.CharField(max_length=45, blank=True, null=True)
    geom = models.CharField(max_length=45, blank=True, null=True)
    description_of_incident = models.CharField(max_length=45, blank=True, null=True)
    photo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'incident'

    def __str__(self):
        return self.incident_type__name

class IncidentType(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'incident_type'

    def __str__(self):
        return self.name

class LandUse(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'land_use'

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    shape_leng = models.CharField(max_length=45, blank=True, null=True)
    shape_area = models.CharField(max_length=45, blank=True, null=True)
    ward = models.ForeignKey('Ward',on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'location'

    def __str__(self):
        return self.name

class SocialAmenity(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    social_amenity_type = models.ForeignKey('SocialAmenityType',on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    long = models.CharField(max_length=45, blank=True, null=True)
    geom = models.CharField(max_length=45, blank=True, null=True)
    ward = models.ForeignKey('Ward',on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'social_amenity'

    def __str__(self):
        return self.name

class SocialAmenityType(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'social_amenity_type'

    def __str__(self):
        return self.name
