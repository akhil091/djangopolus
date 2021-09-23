from django.shortcuts import render
from datetime import datetime
from .models import *

def index(request):
    return render(request,"index.html")

def bds(request):
    return render(request,"services/businessdevelopment.html")

def brandingstrategy(request):
    return render(request,"services/businessdevelopment/branding-strategy.html")

def contentstrategy(request):
    return render(request,"services/businessdevelopment/content-strategy.html")

def b2bb2c(request):
    return render(request,"services/businessdevelopment/b2b&b2c.html")

def crm(request):
    return render(request,"services/businessdevelopment/crm&lead-nurturing.html")

def advertising(request):
    return render(request,"services/businessdevelopment/digital&print-advertising.html")

def automation(request):
    return render(request,"services/businessdevelopment/marketing-automation.html")

def bpo(request):
    return render(request,"services/businessdevelopment/bposervices&consulting.html")

def reputationmanagement(request):
    return render(request,"services/reputationmanagement.html")

def online(request):
    return render(request,"services/reputationmanagement/online-reputation.html")

def seo(request):
    return render(request,"services/reputationmanagement/online/seo.html")

def content(request):
    return render(request,"services/reputationmanagement/online/content-solutions.html")

def smo(request):
    return render(request,"services/reputationmanagement/online/smo.html")

def webinar(request):
    return render(request,"services/reputationmanagement/online/online-events&webinar.html")

def blog(request):
    return render(request,"services/reputationmanagement/online/blog-management.html")

def offline(request):
    return render(request,"services/reputationmanagement/offline-reputation.html")

def campaigns(request):
    return render(request,"services/reputationmanagement/offline/campaigns.html")

def road(request):
    return render(request,"services/reputationmanagement/offline/road-shows.html")

def offads(request):
    return render(request,"services/reputationmanagement/offline/off-ads.html")

def seminars(request):
    return render(request,"services/reputationmanagement/offline/seminars&events.html")

def charity(request):
    return render(request,"services/reputationmanagement/offline/charity-shows.html")

def eorg(request):
    return render(request,"ourexpertise/e-org.html")

def political(request):
    return render(request,"ourexpertise/political-org.html")

def businesses(request):
    return render(request,"ourexpertise/businesses.html")

def educationalorg(request):
    return render(request,"ourworkprocess/educationalorg.html")

def politicalorg(request):
    return render(request,"ourworkprocess/politicalorg.html")

def businesshouses(request):
    return render(request,"ourworkprocess/businesshouses.html")

def about(request):
    return render(request,"about/aboutus.html")

def team(request):
    return render(request,"about/team.html")

def whychooseus(request):
    return render(request,"about/whychooseus.html")

def contacts(request):
    thanks = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        Contact1 = Contact(name=name, email=email, phone=phone, message=message)
        Contact1.save()
        thanks = True

    return render(request, 'contact.html', {'thanks': thanks})
