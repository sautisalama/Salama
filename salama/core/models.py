from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


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


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ngo', 'NGO'),
        ('professional', 'Professional'),
        ('survivor', 'Survivor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class NGOProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    service_models = models.TextField()
    # Add other fields as necessary

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    bio = models.TextField()
    availability = models.CharField(max_length=100)
    tokens = models.IntegerField(default=3)

    def confirm_booking(self, appointment):
        if self.tokens > 0:
            appointment.status = 'confirmed'
            appointment.save()
            self.tokens -= 1
            self.save()
            return True
        return False

class Appointment(models.Model):
    professional = models.ForeignKey(ProfessionalProfile, on_delete=models.CASCADE)
    survivor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')
    # Add other fields as necessary