from django.db import models
import uuid

def generate_report_id():
    return 'sauti_salama_' + str(uuid.uuid4())[:8]

class Report(models.Model):
    report_id = models.CharField(primary_key=True, max_length=255, default=generate_report_id)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    submission_timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    country_code = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=255, null=True)
    postcode = models.CharField(max_length=20, null=True)
    continent = models.CharField(max_length=255, null=True)
    continent_code = models.CharField(max_length=10, null=True)
    locality = models.CharField(max_length=255, null=True)
    plus_code = models.CharField(max_length=20, null=True)
    principal_subdivision = models.CharField(max_length=255, null=True)
    principal_subdivision_code = models.CharField(max_length=10, null=True)
    administrative = models.JSONField(null=True)
    location = models.CharField(max_length=255, null=True)
    type_of_incident = models.CharField(max_length=20, choices=[
        ('physical', 'Physical'),
        ('emotional', 'Emotional'),
        ('sexual', 'Sexual'),
        ('financial', 'Financial'),
        ('other', 'Other (please specify)'),
    ], null=True)
    incident_description = models.TextField(null=True)
    urgency = models.CharField(max_length=10, choices=[
        ('high', 'High (Immediate danger)'),
        ('medium', 'Medium (Needs attention soon)'),
        ('low', 'Low (Not urgent)'),
    ], null=True)
    
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=[
        ('female', 'Female'),
        ('male', 'Male'),
        ('non_binary', 'Non-binary'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ], null=True)
    support_services = models.CharField(max_length=255, null=True, choices=[
        ('legal', 'Legal'),
        ('medical', 'Medical'),
        ('mental_health', 'Mental Health'),
        ('shelter', 'Shelter'),
        ('financial_assistance', 'Financial Assistance'),
        ('other', 'Other (please specify)'),
    ])
    preferred_language = models.CharField(max_length=20, choices=[
        ('english', 'English'),
        ('swahili', 'Swahili'),
        ('other', 'Other (please specify)'),
    ], null=True)
    additional_info = models.TextField(null=True)
    contact_preference = models.CharField(max_length=20, choices=[
        ('phone_call', 'Phone Call'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('do_not_contact', 'Do not contact'),
    ], null=True)
    consent = models.CharField(max_length=5, choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
    ], null=True)
    

    def __str__(self):
        return self.report_id
    
class SupportService(models.Model):
    name = models.CharField(max_length=255)
    helpline = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    service_types = models.CharField(max_length=255)  # Comma-separated service types
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    coverage_area_radius = models.FloatField(default=50)  # In kilometers
    priority = models.IntegerField(default=0)  # Higher number indicates higher priority

    def __str__(self):
        return self.name
    

class MatchedService(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    service = models.ForeignKey(SupportService, on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report} matched with {self.service}"
