from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_report', views.CreateReportView.as_view(), name='create_report'),
    path('matched_services/<int:report_id>/', views.matched_services_view, name='matched_services'),
    path('create_ngo_profile/', views.create_ngo_profile, name='create_ngo_profile'),
    path('create_professional_profile/', views.create_professional_profile, name='create_professional_profile'),
    path('list_professionals/', views.list_professionals, name='list_professionals'),
    path('professionals/', views.list_professionals, name='list_professionals'),
    path('book_appointment/<int:professional_id>/', views.book_appointment, name='book_appointment'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('professional_bookings/', views.professional_bookings, name='professional_bookings'),
]