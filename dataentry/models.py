from django.db import models

class Company(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    located_in = models.CharField(max_length=255, blank=True, null=True)
    pricing = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    contact_us = models.URLField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    num_reviews = models.CharField(max_length=50, blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # You can store URLs as comma-separated strings
    business_hours = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    google_maps_link = models.URLField(blank=True, null=True)
    google_my_maps_link = models.URLField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
