from django.db import models
import uuid

class Report(models.Model):
    report_id = models.CharField(primary_key=True, max_length=255, default='sauti_salama_' + str(uuid.uuid4())[:8])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    continent = models.CharField(max_length=255)
    continent_code = models.CharField(max_length=10)
    locality = models.CharField(max_length=255)
    plus_code = models.CharField(max_length=20)
    principal_subdivision = models.CharField(max_length=255)
    principal_subdivision_code = models.CharField(max_length=10)
    administrative = models.JSONField()

    def __str__(self):
        return self.report_id
