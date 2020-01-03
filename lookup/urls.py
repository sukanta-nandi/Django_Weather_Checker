from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'), # Home page URL
   path('about', views.about, name="about"), #About Page URL
]
