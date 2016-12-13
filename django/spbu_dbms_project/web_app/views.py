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
import numpy as np
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from dicttoxml import dicttoxml as xmlify
from xml.dom.minidom import parseString
import re
from dateutil.relativedelta import relativedelta
# Create your views here.

def index(request):
    username = auth.get_user(request).username
    if (username):
        return render_to_response('index.html')
    else:
        return redirect("/login")

def about(request):
    username = auth.get_user(request).username
    if (username):
        return render_to_response('about.html')
    else:
        return redirect("/login")

def login(request):
    username = auth.get_user(request).username
    if (username):
        return redirect('/')
    else:
        args = {}
        args.update(csrf(request))
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
                args['login_error'] = format_html("<div class=\"main-error alert alert-error\">Неправильное имя пользователя или пароль</div>")
                return render_to_response('login.html', args)
        else:
            return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")
#----

#----
def history(request):
    username = auth.get_user(request).username
    if (username):
        сt = city.objects.all().values()
        co = country.objects.all().values()

        city_json = json.dumps(list(сt), cls=DjangoJSONEncoder,ensure_ascii=False)
        country_json = json.dumps(list(co), cls=DjangoJSONEncoder,ensure_ascii=False)
        args={}
        args['city']=city_json
        args['country'] = country_json
        args['max_date'] = []
        for i in сt:
            args['max_date'].append((temperature.objects.filter(city_id__exact=i['city_id']).latest('date').date))
        return render_to_response("history.html",args)
    else:
        return redirect("/login")

@csrf_exempt
def historyQuery(request):
    username = auth.get_user(request).username
    if (username):
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
            dom=parseString(xmlify(d_temperature, custom_root='weather',attr_type=False)).toprettyxml();
            dom=re.sub('\n+', '', dom)
            args['xml']= format_html(dom)

            return render_to_response("q_history.html", args)
        return redirect('/history')
    else:
        return redirect("/login")

def forecast(request):
    username = auth.get_user(request).username
    if (username):
        сt = city.objects.all().values()
        co = country.objects.all().values()

        city_json = json.dumps(list(сt), cls=DjangoJSONEncoder,ensure_ascii=False)
        country_json = json.dumps(list(co), cls=DjangoJSONEncoder,ensure_ascii=False)
        args={}
        args['city']=city_json
        args['country'] = country_json
        args['max_date']=[]
        for i in сt:
            args['max_date'].append((temperature.objects.filter(city_id__exact = i['city_id']).latest('date').date))

        #args['max_date'] = (temperature.objects.filter(city_id__exact=city).latest('date').date)
        return render_to_response("forecast.html",args)
    else:
        return redirect("/login")

@csrf_exempt
def forecastQuery(request):
    username = auth.get_user(request).username
    if (username):
        args = {}
        if request.POST:
            city=request.POST.get('city', '')
            date_to = request.POST.get('date_to','')
           # minus_year=datetime.timedelta(days=36524.25)
            date_del=datetime.datetime.strptime(date_to,'%Y-%m-%d')
            min_date=temperature.objects.filter(city_id__exact=city).earliest('date').date
            T=[]
            P = []
            U = []

            while date_del>=min_date:
                date_del= date_del - relativedelta(years=1)
                tmp_T=list(temperature.objects.filter(date__gte=date_del, date__lt=date_del+relativedelta(days=1), city_id__exact=city).order_by('date').values('T','date'))
                tmp_P = list(pressure.objects.filter(date__exact=date_del, city_id__exact=city).order_by('date').values('P'))
                tmp_U = list(other_weather_data.objects.filter(date__exact=date_del, city_id__exact=city).order_by('date').values('U'))
                av = []
                for i in tmp_T:
                    try: av.append(float(i['T']))
                    except: continue
                av=np.average(np.array(av))
                T.append(av)
                av = []
                for i in tmp_P:
                    try: av.append(float(i['P']))
                    except: continue
                av = np.average(np.array(av))
                P.append(av)
                av = []
                for i in tmp_U:
                    try:av.append(float(i['U']))
                    except: continue
                av = np.average(np.array(av))
                U.append(av)
            T.reverse()
            P.reverse()
            U.reverse()
            print(T)
            T=np.array(T[1:len(T)])
            P=np.array(P[1:len(P)])
            U=np.array(U[1:len(U)])

            x_t = np.linspace(0, T.size - 1, T.size)
            x_p = np.linspace(0, P.size - 1, P.size)
            x_u = np.linspace(0, U.size - 1, U.size)

            res_T = np.polyfit(x_t, T, 4)
            res_P = np.polyfit(x_p, P, 4)
            res_U = np.polyfit(x_u, U, 4)
            T_1 = np.polyval(res_T, T.size)
            P_1 = np.polyval(res_P,P.size)
            U_1 = np.polyval(res_U,U.size)
            print(T_1,P_1,U_1)

            date_tmp=datetime.datetime.strptime(date_to,'%Y-%m-%d')-datetime.timedelta(days=60)

            T_t = (list(temperature.objects.filter(date__gte=date_tmp, date__lte=date_to,city_id__exact=city).order_by('date').values('T')))
            P_p = (list(pressure.objects.filter(date__gte=date_tmp, date__lte=date_to, city_id__exact=city).order_by('date').values('P')))
            U_u = (list(other_weather_data.objects.filter(date__gte=date_tmp, date__lte=date_to, city_id__exact=city).order_by('date').values('U')))
            for a, b, c, in zip(T_t, P_p, U_u):
                a.update(b)
                a.update(c)

            T=[]
            P=[]
            U=[]
            for i in T_t:
                try:T.append(float(i['T']))
                except: print()
                try:P.append(float(i['P']))
                except: print()
                try: U.append(float(i['U']))
                except: print()

            T=np.array(T)
            P = np.array(P)
            U = np.array(U)

            x_t = np.linspace(0, T.size - 1, T.size)
            x_p = np.linspace(0, P.size - 1, P.size)
            x_u = np.linspace(0, U.size - 1, U.size)
            res_T = np.polyfit(x_t, T, 4)
            res_P = np.polyfit(x_p, P, 4)
            res_U = np.polyfit(x_u, U, 4)
            T = ((np.polyval(res_T, T.size+4)))
            P = ((np.polyval(res_P, P.size+4)))
            U = ((np.polyval(res_U, U.size+4)))
            print(T,P,U)
            T = np.average([ T])
            P = np.average([ P])
            U = np.average([ U])
            date_to=datetime.datetime.strptime(date_to, '%Y-%m-%d')
            args['date']=date_to.date()
            args['T'] = str(T)
            args['P'] = str(P)
            args['U'] = str(U)
            return render_to_response("q_forecast.html", args)
        return redirect('/forecast')
    else:
        return redirect("/login")

def register(request):
    username = auth.get_user(request).username
    if not (username):
        args={}
        args.update(csrf(request))
        args['form']=UserCreationForm()
        if request.POST:
            newuser_form=UserCreationForm(request.POST)
            if newuser_form.is_valid():
                newuser_form.save()
                newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password2'])
                auth.login(request, newuser)
                return redirect('/')
            else:
                args['errors'] = format_html('<div class="main-error alert alert-error">Ошибка при регистрации</div>')
                args['form'] = newuser_form
        return render_to_response('register.html',args)
    else:
        return redirect('/')