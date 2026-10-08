# list of all the allowable URLs that can be accessed for this app
from django.urls import path

from . import views

urlpatterns = [
    # set view should renedred when this url is visited
    path("", views.index, name="index")    
] 