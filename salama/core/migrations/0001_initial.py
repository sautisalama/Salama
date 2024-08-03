# Generated by Django 5.0.2 on 2024-07-31 12:30

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.CharField(default=core.models.generate_report_id, max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('submission_timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('country_code', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('postcode', models.CharField(max_length=20, null=True)),
                ('continent', models.CharField(max_length=255, null=True)),
                ('continent_code', models.CharField(max_length=10, null=True)),
                ('locality', models.CharField(max_length=255, null=True)),
                ('plus_code', models.CharField(max_length=20, null=True)),
                ('principal_subdivision', models.CharField(max_length=255, null=True)),
                ('principal_subdivision_code', models.CharField(max_length=10, null=True)),
                ('administrative', models.JSONField(null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('type_of_incident', models.CharField(choices=[('physical', 'Physical'), ('emotional', 'Emotional'), ('sexual', 'Sexual'), ('financial', 'Financial'), ('other', 'Other (please specify)')], max_length=20, null=True)),
                ('incident_description', models.TextField(null=True)),
                ('urgency', models.CharField(choices=[('high', 'High (Immediate danger)'), ('medium', 'Medium (Needs attention soon)'), ('low', 'Low (Not urgent)')], max_length=10, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('non_binary', 'Non-binary'), ('prefer_not_to_say', 'Prefer not to say')], max_length=20, null=True)),
                ('support_services', models.CharField(choices=[('legal', 'Legal'), ('medical', 'Medical'), ('mental_health', 'Mental Health'), ('shelter', 'Shelter'), ('financial_assistance', 'Financial Assistance'), ('other', 'Other (please specify)')], max_length=255, null=True)),
                ('preferred_language', models.CharField(choices=[('english', 'English'), ('swahili', 'Swahili'), ('other', 'Other (please specify)')], max_length=20, null=True)),
                ('additional_info', models.TextField(null=True)),
                ('contact_preference', models.CharField(choices=[('phone_call', 'Phone Call'), ('sms', 'SMS'), ('email', 'Email'), ('do_not_contact', 'Do not contact')], max_length=20, null=True)),
                ('consent', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
            ],
        ),
    ]
