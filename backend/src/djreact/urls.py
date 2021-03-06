"""djreact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

from django.contrib import admin
from econnect import  views as eviews
from users import  views as uviews
from django.contrib.auth import views as auth_views
from econnect.views import TrainingDetailView, TrainingListView, UpdateTrainingView, MakeTrainingView

from django.conf import  settings
from django.conf.urls.static import  static

urlpatterns = [



    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', eviews.home, name = 'home'),
    url(r'^profile/',eviews.profile, name = 'profile'),
    url(r'^register/',eviews.register, name = "register"),
    
    url(r'^training/edit/(?P<pk>\d+)',UpdateTrainingView.as_view(),name='edit_training'),
    url(r'^editprofile/',eviews.editprofile,name='editprofile'),
    url(r'^training/new',MakeTrainingView.as_view(),name='make_training'),
    url(r'^dashboard/', TrainingListView.as_view(), name = 'dashboard'),
    url(r'^training/(\d+)', eviews.training_details , name = 'training_detail'),
  
    url(r'^login/',auth_views.LoginView.as_view(template_name = 'login.html'), name = "login"),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name = "logout"),
   
    url(r'^click/(\d+)',eviews.enroll,name = 'enroll'),
    url(r'^leaving/(\d+)',eviews.leave,name = 'leave'),
    url(r'^complete/(\d+)',eviews.complete,name = 'complete'),

    # url(r"^register/", uviews.register),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
