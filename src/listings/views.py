from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def base(request):
    return render(request, 'base.html')

def base2(request):
    return render(request, 'base2.html')

def hello(request):
    bands = Band.objects.all()
    return render(request, 'hello.html', {'bands': bands} )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def help_page(request):
    return render(request, 'help_page.html')

def connection(request):
    return render(request, 'connection.html')


