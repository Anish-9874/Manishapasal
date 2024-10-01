from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect


# create your views here

def rice_details(request):
    return render(request,'rice_details.html')



def maida_details(request):
    return render(request,'maida_details.html')

def oil_details(request):
    return render(request,'oil_details.html')




# Home page view
def home(request):
    return render(request, 'index.html')

# About page view
def aboutus(request):
    return render(request, 'aboutus.html')

# Services page view
def services(request):
    return render(request, 'services.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')


# About page view
def aboutme(request):
    return render(request, 'aboutme.html')

