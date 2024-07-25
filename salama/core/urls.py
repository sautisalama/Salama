from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_report', views.CreateReportView.as_view(), name='create_report'),
]
