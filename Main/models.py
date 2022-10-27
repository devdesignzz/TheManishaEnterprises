from re import T
from django.db import models
from ckeditor.fields import RichTextField
from .helpers import *

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimony = models.TextField()
    photo = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Gallery(models.Model):

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pics/gallery')

    def __str__(self):
        return self.name

class HomePageScroll(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='pics/banner')

    def __str__(self):
        return self.Name

class Service(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pics/service')

    def __str__(self):
        return self.name

mode_choices = (
        ("12", 'Landscape'),
        ("4", 'Portrait')
    )

class Project(models.Model):

    project_name = models.CharField(max_length=500)
    project_heading = models.CharField(max_length=500)
    project_image_1 = models.ImageField(upload_to='pics/project')
    project_image_2 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_3 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_4 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_5 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    image_mode = models.CharField(max_length=2, choices = mode_choices)
    project_detail = RichTextField()

    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.project_name)
        super(Project, self).save(*args, **kwargs)

    
class RecentProject(models.Model):

    project_name = models.CharField(max_length=500)
    project_heading = models.CharField(max_length=500)
    project_image_1 = models.ImageField(upload_to='pics/project')
    project_image_2 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_3 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_4 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    project_image_5 = models.ImageField(upload_to='pics/project', null=True, blank=True)
    image_mode = models.CharField(max_length=2, choices = mode_choices)
    project_detail = RichTextField()

    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        self.slug = generate_slug_2(self.project_name)
        super(RecentProject, self).save(*args, **kwargs)


class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WebsiteDetail(models.Model):

    homepage_heading = models.CharField(max_length=200)
    homepage_description = models.TextField()

    homepage_about_us = RichTextField()

    On_Going_Project_Heading = models.CharField(max_length=200)
    On_Going_Project_Description = models.TextField()

    gallery_heading = models.CharField(max_length=200)
    gallery_description = models.TextField()

    bottom_contact_detail = models.TextField()
    about_company_footer = RichTextField()

    about_page_heading = models.CharField(max_length=200)

    about_first_image = models.ImageField(upload_to='pics/about')
    about_first_detail = RichTextField()
    about_second_image = models.ImageField(upload_to='pics/about')
    about_second_detail = RichTextField()

    phone_number = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=50)
    short_address = models.CharField(max_length=150)

    
    linked_by = models.CharField(max_length=15)

    def __str__(self):
        return self.linked_by + " | Do not add delete this or add any more" 