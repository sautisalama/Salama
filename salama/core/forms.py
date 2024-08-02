from django import forms
from .models import Report
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['first_name', 'last_name', 'email', 'phone', 'location', 'type_of_incident', 'incident_description', 'urgency', 'dob', 'gender', 'support_services', 'preferred_language', 'additional_info', 'contact_preference', 'consent']