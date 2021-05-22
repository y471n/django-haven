from django.shortcuts import render
from .utils import fetch_property_price, get_cached_api_data
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core import serializers

# TODO: If time remains, move to Django-RestFramework
def handle_property_request(request, endpoint: int = None):
    propertyId = request.GET.get('propertyId', None)
    if not propertyId:
        return HttpResponseBadRequest()
    p, created = get_cached_api_data(propertyId)
    if not created:
        fetch_from_any_endpoint = bool(endpoint)
        result, endpoint = fetch_property_price(fetch_from_any_endpoint, propertyId, endpoint)
        
        p.status = result['status']
        p.value = result.get('value', '')
        p.fetched_from = str(endpoint)
        p.save()
    serialized_obj = serializers.serialize('json', [ p ])
    # TODO: Handle cases for no API Results
    return JsonResponse({'status': p.status, 'value': p.value})

def index(request):
    return handle_property_request(request)    

# TODO: Handle with a decorator
def select_endpoint(request):
    endpoint = request.GET.get('endpoint', None)
    if not endpoint:
        return HttpResponseBadRequest()
    return handle_property_request(request, int(endpoint))


