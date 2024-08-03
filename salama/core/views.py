import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Report, ProfessionalProfile, Appointment
from .forms import AppointmentForm, CustomUserCreationForm, ReportForm, NGOProfileForm, ProfessionalProfileForm, CustomUserForm
import json
from .utils import match_support_service
from django.contrib import messages
import pandas as pd
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CreateReportView(View):
    def get(self, request):
        form = ReportForm()
        return render(request, 'report.html', {'form': form})

    def post(self, request):
        try:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                data = json.loads(request.body)
                form = ReportForm(data)
                if form.is_valid():
                    report = form.save(commit=False)
                    report.latitude = data['latitude']
                    report.longitude = data['longitude']
                    report.state = data['state']
                    report.country = data['country']
                    report.country_code = data['countryCode']
                    report.city = data['city']
                    report.postcode = data['postcode']
                    report.continent = data['continent']
                    report.continent_code = data['continentCode']
                    report.locality = data['locality']
                    report.plus_code = data['plusCode']
                    report.principal_subdivision = data['principalSubdivision']
                    report.principal_subdivision_code = data['principalSubdivisionCode']
                    report.administrative = data['administrative']
                    report.save()

                    matched_services = match_support_service(report)
                    if matched_services:
                        return JsonResponse({'message': 'Report created successfully and matched with a service.'})
                    else:
                        return JsonResponse({'message': 'Report created successfully but no matching service found.'})
                else:
                    return JsonResponse({'error': 'Invalid form data', 'form_errors': form.errors}, status=400)
            else:
                form = ReportForm(request.POST)
                if form.is_valid():
                    report = form.save()
                    matched_services = match_support_service(report)
                    messages.success(request, 'Report created successfully.')
                    return redirect('matched_services', report_id=report.id)
                else:
                    return render(request, 'report.html', {'form': form})
        except Exception as e:
            logger.exception("Error occurred while creating report")
            return JsonResponse({'error': 'An error occurred', 'details': str(e)}, status=500)

def matched_services_view(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    matched_services = report.matched_services.all()

    return render(request, 'matched_services.html', {
        'report': report,
        'matched_services': matched_services
    })

@login_required
def create_ngo_profile(request):
    if request.user.user_type != 'ngo':
        messages.error(request, 'You are not authorized to create an NGO profile.')
        return redirect('home')

    if request.method == 'POST':
        form = NGOProfileForm(request.POST)
        if form.is_valid():
            ngo_profile = form.save(commit=False)
            ngo_profile.user = request.user
            ngo_profile.save()
            return redirect('home')
    else:
        form = NGOProfileForm()
    return render(request, 'create_ngo_profile.html', {'form': form})

@login_required
def create_professional_profile(request):
    if request.user.user_type != 'professional':
        messages.error(request, 'You are not authorized to create a professional profile.')
        return redirect('home')

    if request.method == 'POST':
        form = ProfessionalProfileForm(request.POST)
        if form.is_valid():
            professional_profile = form.save(commit=False)
            professional_profile.user = request.user
            professional_profile.save()
            return redirect('home')
    else:
        form = ProfessionalProfileForm()
    return render(request, 'create_professional_profile.html', {'form': form})

def list_professionals(request):
    professionals = ProfessionalProfile.objects.all().order_by('-tokens')
    return render(request, 'list_professionals.html', {'professionals': professionals})

@login_required
def book_appointment(request, professional_id):
    professional = get_object_or_404(ProfessionalProfile, id=professional_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.professional = professional
            appointment.survivor = request.user
            appointment.status = 'pending'
            appointment.save()
            return redirect('list_professionals')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'professional': professional})

@login_required
def edit_profile(request):
    user = request.user
    if user.user_type == 'ngo':
        profile_form = NGOProfileForm(instance=user.ngoprofile)
    elif user.user_type == 'professional':
        profile_form = ProfessionalProfileForm(instance=user.professionalprofile)
    else:
        profile_form = None

    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=user)
        if profile_form:
            profile_form = profile_form.__class__(request.POST, instance=profile_form.instance)
        if user_form.is_valid() and (not profile_form or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('edit_profile')
    else:
        user_form = CustomUserForm(instance=user)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def professional_bookings(request):
    if request.user.user_type != 'professional':
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

    professional = request.user.professionalprofile
    appointments = Appointment.objects.filter(professional=professional, status='pending')

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id, professional=professional)
        if professional.confirm_booking(appointment):
            messages.success(request, 'Appointment confirmed.')
        else:
            messages.error(request, 'Not enough tokens to confirm the appointment.')

    return render(request, 'professional_bookings.html', {
        'appointments': appointments,
        'tokens': professional.tokens,
    })

def list_professionals(request):
    professionals = ProfessionalProfile.objects.all().order_by('-tokens')
    return render(request, 'list_professionals.html', {'professionals': professionals})