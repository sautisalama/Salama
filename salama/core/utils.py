from geopy.distance import geodesic
from .models import SupportService, MatchedService

def match_support_service(report):
    services = SupportService.objects.all()
    matched_services = []

    report_location = (report.latitude, report.longitude)
    report_service_types = report.support_services.split(',')
    for service in services:
        service_location = (service.latitude, service.longitude)
        distance = geodesic(report_location, service_location).kilometers

        if distance <= service.coverage_area_radius:
            service_types = service.service_types.split(',')
            if any(service_type in report_service_types for service_type in service_types):
                matched_services.append((service, distance))

    # Sort services by distance and priority
    matched_services.sort(key=lambda x: (x[1], -x[0].priority))
    matched_services = [service for service, _ in matched_services]

    # Save matched services in the database
    for service in matched_services[:5]:  # Limit to top 5 matches
        MatchedService.objects.create(report=report, service=service)

    return matched_services
 