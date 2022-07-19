from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('help/', views.help_page),
    path('base2/', views.base2),
    path('base/', views.base),
    path('connection/', views.connection, name='connection'),

]