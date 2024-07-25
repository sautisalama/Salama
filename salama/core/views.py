import logging
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Report
from .forms import ReportForm
import json

# logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

class CreateReportView(View):
    def get(self, request):
        return render(request, 'report.html')

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
                    # report.informative = data['informative']
                    report.save()
                    return JsonResponse({'message': 'Report created successfully'})
                else:
                    return JsonResponse({'error': 'Invalid form data', 'form_errors': form.errors}, status=400)
            else:
                form = ReportForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home')
                else:
                    return render(request, 'report.html', {'form': form})
        except Exception as e:
            logger.exception("Error occurred while creating report")
            return JsonResponse({'error': 'An error occurred', 'details': str(e)}, status=500)
