"""
URL configuration for manishapasal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    


    path('', views.home, name='home'),             # Home page
    path('about/', views.aboutus, name='about'),     # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),# Contact page
    path('aboutme/', views.aboutme, name='aboutme'),



    path('rice/', views.rice_details, name='rice_details'),
    path('maida/', views.maida_details, name='maida_details'),
    path('oil/', views.oil_details, name='oil_details'),
    
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)