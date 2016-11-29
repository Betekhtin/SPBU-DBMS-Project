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
            date_from= request.POST.get('date_from','')
            date_to = request.POST.get('date_to','')
            #date_to = date_to + ' 23:00:00'

            date_tmp=datetime.datetime.strptime(date_to,'%Y-%m-%d')-datetime.timedelta(days=60)

            T_t = (list(temperature.objects.filter(date__gte=date_tmp, date__lte=date_to,city_id__exact=city).order_by('date').values('T')))
            P_p = (list(pressure.objects.filter(date__gte=date_tmp, date__lte=date_to, city_id__exact=city).order_by('date').values('P')))
            U_u = (list(other_weather_data.objects.filter(date__gte=date_tmp, date__lte=date_to, city_id__exact=city).order_by('date').values('U')))
            for a, b, c, in zip(T_t, P_p, U_u):
                a.update(b)
                a.update(c)

            #  a.update(e)
            #  a.update(f)
            T=[]
            P=[]
            U=[]
            for i in T_t:
                T.append(i['T'])
                P.append(i['P'])
                U.append(i['U'])
            tmp = np.array([481, 482, 483, 484, 485, 486, 487, 488])
            T=np.array(T)
            P = np.array(P)
            U = np.array(U)
            x = np.linspace(0, T.size - 1, T.size)
            res_T = np.polyfit(x, T, 4)
            res_P = np.polyfit(x, P, 4)
            res_U = np.polyfit(x, U, 4)
            T = (np.average(np.polyval(res_T, tmp)))
            P = (np.average(np.polyval(res_P, tmp)))
            U = (np.average(np.polyval(res_U, tmp)))
            date_to=datetime.datetime.strptime(date_to, '%Y-%m-%d')

            args['date']=date_to.date()
            args['T'] = str(T)
            args['P'] = str(P)
            args['U'] = str(U)
            # for a,b,c,d,e,f in zip(d_temperature, d_pressure,d_weather,d_clouds,d_other_weather_data,d_wind):
            #  a.update(b)
            #  a.update(c)
            #  a.update(d)
            #  a.update(e)
            #  a.update(f)
            # args['data'] = d_temperature
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