from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    url = models.URLField(max_length=200)
    website_title = models.CharField(max_length=200)
    admin_address = models.TextField()
    admin_email = models.EmailField(max_length=200)
    facebook = models.URLField(max_length=200)
    google_plus = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    website_logo = models.ImageField(upload_to='settings/logo')
    banner_image = models.ImageField(upload_to='settings/banner')


    def __str__(self):
        return self.website_title

class Cms(models.Model):
    about_us = models.TextField()
    our_services = models.TextField()
    terms = models.TextField()
    contact_address = models.TextField()
    contact_number = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_address

class AddBanner(models.Model):
    banner_image = models.ImageField(upload_to='settings/banner')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.link