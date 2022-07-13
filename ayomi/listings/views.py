from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse('À propos</h1> <p>Nous adorons merch !')

def contact(request):
    return HttpResponse('<h1>Contact us</h1>')


def help_page(request):
    return HttpResponse('<h1>help us</h1>')
