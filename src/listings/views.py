from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'hello.html', {'bands': bands} )

def about(request):
    return HttpResponse('À propos</h1> <p>Nous adorons merch !')

def contact(request):
    return HttpResponse('<h1>Contact us</h1>')


def help_page(request):
    return HttpResponse('<h1>help us</h1>')
