from django.contrib import admin
from .models import Gallery, Service, WebsiteDetail, Project, Email, Testimonial, RecentProject, HomePageScroll

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Service)
admin.site.register(WebsiteDetail)
admin.site.register(Project)
admin.site.register(Email)
admin.site.register(Testimonial)
admin.site.register(RecentProject)
admin.site.register(HomePageScroll)