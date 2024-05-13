from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_demand, name="demand"),
    path('course_description/', views.course_description, name='course_description')
]