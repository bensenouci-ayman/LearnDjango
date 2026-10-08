# list of all the allowable URLs that can be accessed for this app
from django.urls import path

from . import views

urlpatterns = [
    # set view should renedred when this url is visited
    # default route
    path("", views.index, name="index"),
    # brian route
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("ayman", views.ayman, name="ayman")
] 