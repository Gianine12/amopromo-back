from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from decouple import config
from datetime import datetime

from .models import Airport
from .serializers import AirportSerializer
from .utils.haversine import haversine

@api_view(http_method_names=['get'])
def get_airpot(request):
    airport = Airport.objects.all()

    serializerAirport = AirportSerializer(instance=airport, many=True)

    return Response(serializerAirport.data)

@api_view(http_method_names=['post'])
def search_ticket_airline(request):
    data = request.data
    print(data)

    url = config('MOCK_AIRLINES_URL') + config('MOCK_AIRLINES_APIKEY') + '/' + data['departure_airport'] + '/' + data['arrival_airport'] + '/' + data['departure_date'] 

    req = requests.get(url,auth=(config('DOMESTIC_AIRPORTS_LOGIN'), config('DOMESTIC_AIRPORTS_SENHA')))
    resp = req.json()

    range = haversine(data['lat1'],data['long1'],data['lat2'],data['long2'])

    # CALCULO DO PRICE
    for i in resp['options']:
        price = i['price']
        valor = price['fare']
        porcentagem = 10

        total = round((valor * porcentagem) / 100,2)

        if total <= 40:
            price['fees'] = 40.00
        else:
            price['fees'] = total
        
        price['total'] = price['fare'] + price['fees']

    # CALCULO DA META
        meta = i['meta']
        meta['range'] = range
        meta['cost_per_km'] = round((price['fare'] * 1) / range,2) 


        hoursArrival = i['arrival_time'].split('T')[1].split(':')
        hoursDeparture = i['departure_time'].split('T')[1].split(':')

        hora = abs(int(hoursArrival[0]) - int(hoursDeparture[0]))
        min = abs(int(hoursArrival[1]) - int(hoursDeparture[1]))

        newH = float(str(hora) + '.' + str(min))

        meta['cruise_speed_kmh'] = round(range / newH, 2)

    return Response(resp)

@api_view(http_method_names=['put'])
def activate_or_deactivate_airports(request):
    data = request.data
    
    airport = Airport.objects.get(iata=data['iata'])
    print(airport)

    airport.active = data['active']
    airport.save()

    return Response('sucesso')


@api_view()
def update_airport(request):
    req = requests.get(config('DOMESTIC_AIRPORTS_URL'), auth=(config('DOMESTIC_AIRPORTS_LOGIN'), config('DOMESTIC_AIRPORTS_SENHA')))

    for i in req.json():

        iata = req.json()[i]['iata']
        
        try:
            airport = Airport.objects.get(iata=iata)
        
            airport.obs = ''
            airport.active = True 
            airport.iata = req.json()[i]['iata']
            airport.city = req.json()[i]['city']
            airport.lat = req.json()[i]['lat']
            airport.lon = req.json()[i]['lon']
            airport.state = req.json()[i]['state']
            airport.save()

        except:
            airport = Airport.objects.create(**req.json()[i])
        

    airportall = Airport.objects.all()
    serializerAirport = AirportSerializer(instance=airportall, many=True)

    return Response(serializerAirport.data)
