"""
URL configuration for tut1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from register import views as v

    # the remainder path from the tut1.urls gets passed into here, and thats how to navigate the different pages
urlpatterns = [
    path('admin/', admin.site.urls),
    # add a new path that links to our main url
    # this is if we dont type anything the path, it'll bring us to main.urls
    path('', include("main.urls")),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls"))
]
