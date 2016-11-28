from django.db import models

#Create your models here.
class country(models.Model):
	class Meta():
		db_table = "country"
	country_id = models.AutoField(primary_key=True)
	country_name = models.CharField(max_length=40)
	
class city(models.Model):
	class Meta():
		db_table = "city"
	city_id = models.AutoField(primary_key=True)
	country= models.ForeignKey('country')
	city_name=models.CharField(max_length=40)
#---------------------------------------------------------------
class weather(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "weather"
	weather_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	WW = models.CharField(max_length=100)
	W1 = models.CharField(max_length=100)
	W2 = models.CharField(max_length=100)

class clouds(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "clouds"
	clouds_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	N = models.IntegerField()
	Cl = models.CharField(max_length=100)
	Nh = models.IntegerField()
	H = models.CharField(max_length=100)
	Cm = models.CharField(max_length=100)
	Ch = models.CharField(max_length=100)

class temperature(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "temperature"
	temperature_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	T = models.FloatField()
	Tn = models.FloatField()
	Tx = models.FloatField()
	Td = models.FloatField()
	Tg = models.FloatField()

class pressure(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "pressure"
	pressure_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	P0 = models.FloatField()
	P = models.FloatField()
	Pa = models.FloatField()

class other_weather_data(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "other_weather_data"
	other_weather_data_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	U = models.IntegerField()
	VV = models.FloatField()
	RRR = models.CharField(max_length=45)
	tR=models.IntegerField()
	E = models.CharField(max_length=45)
	E1 = models.CharField(max_length=45)
	sss=models.CharField(max_length=45)

class wind(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "wind"
	wind_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	DD = models.CharField(max_length=45)
	Ff = models.CharField(max_length=45)
	ff10=models.FloatField()
	ff3=models.FloatField()

class forecast(models.Model):
	class Meta():
		unique_together = (('date', 'city'),)
		db_table = "forecast"
	forecast_id = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	city = models.ForeignKey('city')
	T = models.FloatField()
	P = models.FloatField()
	U = models.FloatField()