from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment, CustomUser, Report, NGOProfile, ProfessionalProfile

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['first_name', 'last_name', 'email', 'phone', 'location', 'type_of_incident', 'incident_description', 'urgency', 'dob', 'gender', 'support_services', 'preferred_language', 'additional_info', 'contact_preference', 'consent']

class NGOProfileForm(forms.ModelForm):
    class Meta:
        model = NGOProfile
        fields = ['organization_name', 'service_models']

class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        fields = ['profession', 'bio', 'availability']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date']

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']