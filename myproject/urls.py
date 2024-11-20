"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    # Home page, which redirects to 'saveinfo' view
    path('', views.saveinfo, name='saveinfo'),  # This is the root URL, which will show your 'saveinfo' view

    # Additional URL patterns
    path('saveinfo/', views.saveinfo, name='saveinfo'),  # This will map to the 'saveinfo' view
    path('index/', views.index, name='index'),  # URL to access the 'index' view
    path('Delete/<int:id>/', views.Delete, name='Delete'),  # URL to delete an entry with a specific id
]
