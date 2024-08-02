import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Report
from .forms import ReportForm
import json
from .utils import match_support_service
from django.contrib import messages
import pandas as pd

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

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


# def display_matched_services(request):
#     matched_services = MatchedService.objects.all()
#     df = pd.read_json()(matched_services)
#     context = {
#         'matched_services': df.to_html(index=False)
#     }
#     return render(request, 'display_matched_services.html', context)
