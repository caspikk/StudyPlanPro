"""
URL configuration for StudyPlanPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Added for OAuth
    path('accounts/', include('allauth.urls')),
    
    # Authentication
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    
    # Other Pages
    path('demand/cs/', include('demand.urls')), #cs demand
    path('demand/comeng/', include('demand2.urls')), #comeng demand
    path('flowchart/cs/', include('flowchart.urls')), #cs flowchart
    path('flowchart/comeng/', include('flowchart2.urls')), #comeng flowchart
]
