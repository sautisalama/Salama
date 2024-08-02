from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_report', views.CreateReportView.as_view(), name='create_report'),
    path('matched_services/<int:report_id>/', views.matched_services_view, name='matched_services'),
    # path('display_matched_services/', views.display_matched_services, name='display_matched_services'),

]
