from django.shortcuts import render
from .models import Gallery, Service, WebsiteDetail, Project, Email, Testimonial, RecentProject, HomePageScroll
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def error_404_view(request, exception):

    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]

    return render(request, '404.html', {"first_five_services": first_five_services, 'website':website})

def error_500_view(request, *args, **argv):
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]

    return render(request, '404.html', {"first_five_services": first_five_services, 'website':website})



def index(request):

    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    reviews = Testimonial.objects.all()[::-1]
    first_five_services = services[:3]
    first_six_services = services[:6]
    photos = Gallery.objects.all()[:3][::-1]
    recent_working_projects = RecentProject.objects.all()[::-1]
    background = HomePageScroll.objects.all()
    return render(request ,"index.html", {"first_five_services": first_five_services, 
    'website':website, 'first_six_services':first_six_services,"photos":photos, 'reviews':reviews, 
    'working_projects':recent_working_projects, "background":background})


def contact(request):

    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]
    email_ob = Email.objects.all()
    email_ls = []

    for e in email_ob:
        email_ls.append(e.email)

    if request.method == "POST":
        message_name = request.POST['firstName']
        message_subject = request.POST['subjectName']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message_message = request.POST['msg']
        email = settings.EMAIL_HOST_USER

        send_mail(
            message_subject + " | " + message_name,
            message_message + "\n\nPhone : " + message_phone + "\nEmail : " + message_email,
            email,
            email_ls
        )


        return render(request, "contact.html", {"message":message_name, "first_five_services": first_five_services, 'website':website})
    else:
        return render(request, "contact.html",  {"first_five_services": first_five_services, 'website':website})


def about(request):

    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]

    return render(request, 'about.html', {'website':website, "first_five_services": first_five_services})


def services(request):

    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]

    return render(request, 'services.html', {"services":services, 'website':website, "first_five_services": first_five_services})


def portfolio(request):
    projects = Project.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]
    return render(request, 'portfolio.html', {"projects":projects, "first_five_services": first_five_services, 'website':website})


def portfoliodetail(request, slug):
    project = Project.objects.get(slug=slug)
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]
    return render(request, 'portfolio-detail.html', {'project':project, "first_five_services": first_five_services, 'website':website})

def GoingProject(request, slug):
    project = RecentProject.objects.get(slug=slug)
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]
    return render(request, 'portfolio-detail.html', {'project':project, "first_five_services": first_five_services, 'website':website})


def gallery(request):
    photos = Gallery.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    services = Service.objects.all()
    first_five_services = services[:3]
    return render(request, 'gallery.html', {"photos":photos, "first_five_services": first_five_services, 'website':website})