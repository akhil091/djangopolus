from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('business-development',views.bds,name="business-development"),
    path('content-strategy',views.contentstrategy,name="content-strategy"),
    path('branding-strategy',views.brandingstrategy,name="branding-strategy"),
    path('b2b-b2c',views.b2bb2c,name="b2b-b2c"),
    path('crm-and-lead-nurturing',views.crm,name="crm-and-lead-nurturing"),
    path('digital-and-print-advertising',views.advertising,name="digital-and-print-advertising"),
    path('marketing-automation',views.automation,name="marketing-automation"),
    path('bpo-services-and-consulting',views.bpo,name="bpo-services-and-consulting"),
    path('reputation-management',views.reputationmanagement,name="reputation-management"),
    path('content-solutions',views.content,name='content-solutions'),
    path('smo',views.smo,name='smo'),
    path('webinar-and-events',views.webinar,name='webinar-and-events'),
    path('blog-management',views.blog,name='blog-management'),
    path('campaigns',views.campaigns,name='campaigns'),
    path('road-shows',views.road,name='road-shows'),
    path('offline-ads',views.offads,name='offline-ads'),
    path('seminars',views.seminars,name='seminars'),
    path('charity-shows',views.charity,name='charity-shows'),
    path('expertise/edu-org',views.eorg,name='expertise/edu-org'),
    path('expertise/political-org',views.political,name='expertise/political-org'),
    path('expertise/business-houses',views.businesses,name='expertise/business-houses'),
    path('workprocess/edu-org',views.educationalorg,name='workprocess/edu-org'),
    path('workprocess/political-org',views.politicalorg,name='workprocess/political-org'),
    path('workprocess/business',views.businesshouses,name='workprocess/business'),
    path('aboutus',views.about,name='aboutus'),
    path('our-team',views.team,name='our-team'),
    path('why-choose-us',views.whychooseus,name='why-choose-us'),
    path('contact',views.contacts,name='contact'),
    path('offline-reputation-management',views.offline,name='offline-reputation-management'),
    path('online-reputation-management',views.online,name='online-reputation-management'),
    path('seo',views.seo,name='seo'),


]
