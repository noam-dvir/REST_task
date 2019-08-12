from django.shortcuts import render
from django.http import HttpResponse
from .models import logEntry,counter
from geolite2 import geolite2


def index(request):
    return HttpResponse("<h2>/getID - returns unique request ID</h2><h2>/showDB - display log</h2>")

def showDB(request):
    entries_list = logEntry.objects.order_by('-val')
    context_dict = {'log_entries':entries_list}
    return render(request,'REST_app/displayDB.html',context=context_dict)

def DBID(request):

    #get request id and update stored value
    req_id=FetchAndUpdate()

    #get client ip
    ipaddress = getClientIP(request)

    #get client ua
    user_agent= request.META.get('HTTP_USER_AGENT')

    #get client geolocation
    geo_loc_str = getLatLon(ipaddress)

    #insert new entry to DB
    new_entry = logEntry(ip=ipaddress,ua=user_agent,geo=geo_loc_str,val=req_id)
    new_entry.save()

    return HttpResponse(req_id)


def FetchAndUpdate():
    #Get value from DB
    uniqueId = counter.objects.all()

    #Initialize counter if first request
    if (len(uniqueId)==0):
        counter_init = counter(num='0')
        counter_init.save()

    #increment counter
    count_val= counter.objects.all()[0]

    #update counter
    count_val.num += 1
    count_val.save()
    return count_val.num

def getClientIP(request):
        #check request X_FORWARDED_FOR header for iP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[-1].strip()
        return request.META.get('REMOTE_ADDR')

def getLatLon(ipaddress):
    reader = geolite2.reader()
    loc_data=reader.get('109.66.23.103')
    if (loc_data):
        geo_loc=str(loc_data['location']['latitude']) + ',' + str(loc_data['location']['longitude'])
    else:
        geo_loc=""
    geolite2.close()
    return geo_loc
