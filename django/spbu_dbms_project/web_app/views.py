# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.utils.html import format_html
from web_app.models import city, country
import json
from django.core.serializers.json import DjangoJSONEncoder
from web_app.models import temperature, weather, clouds, pressure, other_weather_data, wind
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
# Create your views here.

def index(request):
    username = auth.get_user(request).username
    if (username):
        return render_to_response('index.html')
    else:
        return redirect("/login")

def about(request):
    return render_to_response('about.html',{'username': auth.get_user(request).username})

def login(request):
    username = auth.get_user(request).username
    if (username):
        return redirect('/')
    else:
        args = {}
        args=(csrf(request))
        if request.POST:
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if not request.POST.get('remember-me', ''):
                    request.session.set_expiry(0)
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = format_html("<div class=\"main-error alert alert-error\">Invalid username or password</div>")
                return render_to_response('login.html', args)
        else:
            return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")
#----

#----
def history(request):
    сt = city.objects.all().values()
    co = country.objects.all().values()

    city_json = json.dumps(list(сt), cls=DjangoJSONEncoder,ensure_ascii=False)
    country_json = json.dumps(list(co), cls=DjangoJSONEncoder,ensure_ascii=False)
    args={}
    args['city']=city_json
    args['country'] = country_json
    return render_to_response("history.html",args)

@csrf_exempt
def historyQuery(request):
    args = {}
    if request.POST:
        country=request.POST.get('country', '')
        city=request.POST.get('city', '')
        date_from=request.POST.get('date_from','')

        date_to=request.POST.get('date_to','')
        date_to = date_to + ' 23:00:00'
        d_temperature= list(temperature.objects.filter(date__gte=date_from, date__lte=date_to,city_id__exact=city).order_by('date').values())
        d_pressure =list(pressure.objects.filter(date__gte=date_from, date__lte=date_to, city_id__exact=city).order_by('date').values())
        d_weather = list(weather.objects.filter(date__gte=date_from, date__lte=date_to, city_id__exact=city).order_by('date').values())
        d_clouds = list(clouds.objects.filter(date__gte=date_from, date__lte=date_to, city_id__exact=city).order_by('date').values())
        d_other_weather_data = list(other_weather_data.objects.filter(date__gte=date_from, date__lte=date_to, city_id__exact=city).order_by('date').values())
        d_wind = list(wind.objects.filter(date__gte=date_from, date__lte=date_to, city_id__exact=city).order_by('date').values())
        # for i in listone:
        #     print(i['date'])
        # for i,j in zip(listone,listtwo):
        #      i.update(j)
        for a,b,c,d,e,f in zip(d_temperature, d_pressure,d_weather,d_clouds,d_other_weather_data,d_wind):
         a.update(b)
         a.update(c)
         a.update(d)
         a.update(e)
         a.update(f)
        args['data'] = d_temperature
    return render_to_response("q_history.html", args)
