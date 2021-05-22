import requests
import random
from .models import Property

PROPERTY_APIS = ['https://odrx4hmnq6.execute-api.us-west-2.amazonaws.com/default/interview_api_endpoint_1', 
'https://ry1jrxwgeg.execute-api.us-west-2.amazonaws.com/default/interview_api_endpoint_2'
]
def fetch_property_price(any: bool, propertyId: str, endpoint: int = 1) -> dict:
    if any:
        fetch_api_url = PROPERTY_APIS[random.randint(0,1)]
    else:
        fetch_api_url = PROPERTY_APIS[endpoint]
    print(fetch_api_url)
    params = {'propertyId': propertyId}
    print(params)
    r = requests.get(fetch_api_url, params)
    result = r.json()
    return result


def cache_api_response(status: str, value: str, fetched_from) -> None:
    property = Property(status=status, value=value, fetched_from=fetched_from)
    property.save()

def get_cached_api_data(propertyId):
    property, created = Property.objects.get_or_create(propertyId='1')
    return property, created