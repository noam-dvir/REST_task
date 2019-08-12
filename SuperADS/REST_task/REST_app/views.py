from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import logEntry,counter
from .serializers import EntrySerializer
import requests
from requests import get


class EntryView(viewsets.ModelViewSet):
    queryset = logEntry.objects.all()
    serializer_class = EntrySerializer


def getID(request):
    counter+=1
    print("counter = "+counter)
    return HttpResponse(counter+"")

def index(request):
    #counter+=1
    counter = request.session.get('counter')
    if not counter:
        counter = 1
    request.session['counter'] = counter+1
    print(counter)
    return HttpResponse(counter)

def DBID(request):
    #Get value to be returned
    uniqueId = counter.objects.all()

    #Initialize counter if first page hit
    if (len(uniqueId)==0):
        counter_init = counter(num='0')
        counter_init.save()

    #increment counter
    count_val= counter.objects.all()[0]
    count_val.num += 1
    count_val.save()

    #save user log entry:

    #check request X_FORWARDED_FOR header for iP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    print (ipaddress)
    print('%%%%%%%%%%%%%%%%%remote: ',request.META.get('REMOTE_ADDR'))
    user_agent= request.META.get('HTTP_USER_AGENT')
    print (user_agent)
    new_entry = logEntry(ip=ipaddress,ua=user_agent,val=count_val.num)
    print(new_entry.ua)
    new_entry.save()

    print("here22222222222222222222")

    my_ip = get('https://api.ipify.org').text
    print('My public IP address is:', my_ip)

    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    print(geo_data)

    geo_request_url2 = 'https://get.geojs.io/v1/ip/geo/' + ipaddress + '.json'
    geo_request2 = requests.get(geo_request_url2)
    geo_data2 = geo_request2.json()
    print(geo_data2)

    return HttpResponse(count_val.num)
