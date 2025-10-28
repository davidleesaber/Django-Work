# in here we define the paths to our different web pages
# in this case the different views

from django.urls import path
from . import views

urlpatterns = [
    # using <int:id> it will look for an integer in the path,
    # then pass it in to the index funtion in views
    path("<int:id>", views.index, name="index"),

    # add a  home page
    path("home/", views.home, name="home"),

    # adding a form 
    path("create/", views.create, name="create"),

    path("view/", views.view, name="view"),

]