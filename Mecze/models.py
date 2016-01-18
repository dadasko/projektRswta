from django.db import models
from django.db.models import F


# Create your models here.
class Zespol(models.Model):
	nazwa = models.CharField(max_length=50)
	opis = models.CharField(max_length=256, default='')

	def rozegrane_spotkania(self):
		return 0+Mecz.objects.filter(gospodarz=self.id).count()+Mecz.objects.filter(gosc=self.id).count()

	def wygrane_spotkania(self):
		return 0+Mecz.objects.filter(gospodarz=self.id, gole_gospodarza__gt=F('gole_goscia')).count()+Mecz.objects.filter(gosc=self.id, gole_goscia__gt=F('gole_gospodarza')).count()

	def zremisowane_spotkania(self):
		res = 0+Mecz.objects.filter(gospodarz=self.id, gole_gospodarza=F('gole_goscia')).count()+Mecz.objects.filter(gosc=self.id, gole_goscia=F('gole_gospodarza')).count()
		return res

	def __str__(self):
		return self.nazwa

	
class Pozycja(models.Model):
	nazwa = models.CharField(max_length=15)

	def __str__(self):
		return self.nazwa

	
class Zawodnik(models.Model):
	zespol = models.ForeignKey(Zespol)
	imie = models.CharField(max_length=50)
	nazwisko = models.CharField(max_length=50)
	pozycja = models.ForeignKey(Pozycja)

	def ilosc_bramek(self):
		return Bramka.objects.filter(zawodnik=self.id).count()

	def __str__(self):
		return self.imie+" "+self.nazwisko

	
class Sklad(models.Model):
	zespol = models.ForeignKey(Zespol)
	nazwa_skladu = models.CharField(max_length=16, blank=True)
	zawodnik_1 = models.ForeignKey(Zawodnik, related_name='z1', default='', null=True)
	pozycja_1 = models.ForeignKey(Pozycja, related_name='zp1', default='', null=True)
	zawodnik_2 = models.ForeignKey(Zawodnik, related_name='z2', default='', null=True)
	pozycja_2 = models.ForeignKey(Pozycja, related_name='zp2', default='', null=True)
	zawodnik_3 = models.ForeignKey(Zawodnik, related_name='z3', default='', null=True)
	pozycja_3 = models.ForeignKey(Pozycja, related_name='zp3', default='', null=True)
	zawodnik_4 = models.ForeignKey(Zawodnik, related_name='z4', default='', null=True)
	pozycja_4 = models.ForeignKey(Pozycja, related_name='zp4', default='', null=True)
	zawodnik_5 = models.ForeignKey(Zawodnik, related_name='z5', default='', null=True)
	pozycja_5 = models.ForeignKey(Pozycja, related_name='zp5', default='', null=True)
	zawodnik_6 = models.ForeignKey(Zawodnik, related_name='z6', default='', null=True)
	pozycja_6 = models.ForeignKey(Pozycja, related_name='zp6', default='', null=True)
	zawodnik_7 = models.ForeignKey(Zawodnik, related_name='z7', default='', null=True)
	pozycja_7 = models.ForeignKey(Pozycja, related_name='zp7', default='', null=True)
	zawodnik_8 = models.ForeignKey(Zawodnik, related_name='z8', default='', null=True)
	pozycja_8 = models.ForeignKey(Pozycja, related_name='zp8', default='', null=True)
	zawodnik_9 = models.ForeignKey(Zawodnik, related_name='z9', default='', null=True)
	pozycja_9 = models.ForeignKey(Pozycja, related_name='zp9', default='', null=True)
	zawodnik_10 = models.ForeignKey(Zawodnik, related_name='z10', default='', null=True)
	pozycja_10 = models.ForeignKey(Pozycja, related_name='zp10', default='', null=True)
	zawodnik_11 = models.ForeignKey(Zawodnik, related_name='z11', default='', null=True)
	pozycja_11 = models.ForeignKey(Pozycja, related_name='zp11', default='', null=True)

	def __str__(self):
		return self.nazwa_skladu
		

class Kolejka(models.Model):
	data = models.DateTimeField(auto_now=False, auto_now_add=False)
	nr_kolejki = models.IntegerField()

	def __str__(self):
		return str(self.nr_kolejki)

	def __unicode__(self):
		return str(self.nr_kolejki)

			
class Mecz(models.Model):
	gospodarz = models.ForeignKey(Zespol, related_name='mecz_gospodarz', verbose_name='Gospodarz')
	gosc = models.ForeignKey(Zespol, related_name='mecz_gosc', verbose_name='Gosc')
	sklad_gospodarza= models.ForeignKey('Sklad', related_name='sklad_gospodarz', verbose_name='Sklad gospodarza', blank=True, null=True)
	sklad_goscia= models.ForeignKey('Sklad', related_name='sklad_goscia', verbose_name='Sklad goscia', blank=True, null=True)
	gole_gospodarza = models.CharField(max_length=2, blank=True)
	gole_goscia = models.CharField(max_length=2, blank=True)
	kolejka = models.ForeignKey(Kolejka,  related_name='kolejka', verbose_name='Nr kolejki')
	uwagi = models.CharField(max_length=128, blank=True)

	def __str__(self):
		return str(self.id)+ ": " + self.gospodarz.nazwa + " - " + self.gosc.nazwa + " / Kolejka " + str(self.kolejka.nr_kolejki)
		
class Bramka(models.Model):
	mecz = models.ForeignKey(Mecz)
	zawodnik = models.ForeignKey(Zawodnik)
	minuta = models.IntegerField()

	def __str__(self):
		return "Mecz: " + self.mecz.gospodarz.nazwa + "-" + self.mecz.gosc.nazwa + " Zawodnik: " + str(self.zawodnik.nazwisko)