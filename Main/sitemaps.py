from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.utils.text import slugify
from .models import Project

class StaticViewSitemap(Sitemap):

    changefreq = 'daily'


    def items(self):
        return ['index', 'contact', 'about', 'services', 'portfolio', 'gallery']

    def location(self, item):
        return reverse(item)


class PortfolioSitemap(Sitemap):

    changefreq = "daily"

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return '/portfolio/%s' % (slugify(obj))
