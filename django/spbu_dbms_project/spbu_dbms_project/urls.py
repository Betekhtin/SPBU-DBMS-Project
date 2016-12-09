"""spbu_dbms_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from web_app import views
from web_app import parser
import datetime
from web_app import models

urlpatterns = [
    url(r'^admin/', admin.site.urls), #zharkov ehjl1122
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^q_history/', views.historyQuery, name='historyQuery'),
    url(r'^history/', views.history, name='history'),
    url(r'^forecast/', views.forecast, name='forecast'),
    url(r'^q_forecast/', views.forecastQuery, name='forecastQuery'),
    url(r'^register/', views.register, name='register'),


]

source_page=[]
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5')
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5_(%D0%92%D0%94%D0%9D%D0%A5)')
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%98%D1%81%D1%82-%D0%AD%D0%BB%D0%BC%D1%85%D0%B5%D1%80%D1%81%D1%82%D0%B5_(%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82)')
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%A1%D0%B0%D0%BD-%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D0%B8%D1%81%D0%BA%D0%BE_(%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82)')
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%9F%D0%B5%D0%BA%D0%B8%D0%BD%D0%B5')
source_page.append('http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%91%D0%B0%D0%BE%D1%88%D0%B0%D0%BD%D0%B5,_%D0%A8%D0%B0%D0%BD%D1%85%D0%B0%D0%B9')
j=1
now = datetime.date.today()
сity = models.city.objects.all().values()
max_date = []

for i in сity:
    max_date.append((models.temperature.objects.filter(city_id__exact=i['city_id']).latest('date').date))
for i in source_page:
    tmp=max_date[j-1].date()
    #print (tmp)
    tmp1=i
    while tmp<(now):

        tmp_=str(tmp).split('-')
        tmp_=tmp_[2]+'-'+tmp_[1]+'-' + tmp_[0]
        parser.parser(tmp_,tmp1,str(j))
        tmp = (tmp + datetime.timedelta(days=1))
    j=j+1