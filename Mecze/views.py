from django.shortcuts import render, get_object_or_404
from .models import Zespol, Zawodnik, Mecz, Bramka, Sklad
import operator
from collections import OrderedDict

def index(request):
	mecz = Mecz.objects.select_related('kolejka','gospodarz', 'gosc')
	return render(request, 'Mecze/index.html', {'mecze': mecz})
	
def teams(request):
	zespoly = Zespol.objects.order_by('nazwa')
	return render(request, 'Mecze/team_all.html', {'zespoly': zespoly})
	
	
def team_detail(request, druzyna):
	zespol = get_object_or_404(Zespol, id=druzyna)
	zawodnicy = Zawodnik.objects.filter(zespol=druzyna).order_by('imie')
	return render(request, 'Mecze/team_detail.html', {'zespol': zespol, 'zawodnicy': zawodnicy})
	
def mecz(request, mecz):
	mecz = get_object_or_404(Mecz, id=mecz)
	bramki = Bramka.objects.select_related('zawodnik').filter(mecz=mecz)
	return render(request, 'Mecze/mecz.html', {'mecz': mecz, 'bramki': bramki})	
	
def strzelcy(request):
	strzelcy_bramek={}
	for zawodnik in Zawodnik.objects.all():
		if(zawodnik.ilosc_bramek() > 0):
			strzelcy_bramek[str(zawodnik)]=zawodnik.ilosc_bramek()
	strzelcy_bramek = sorted(strzelcy_bramek.items(), key=operator.itemgetter(1))
	strzelcy_bramek.reverse()
	return render(request, 'Mecze/strzelcy.html', {'zawodnicy': strzelcy_bramek})

def tabela(request):
	statystyki = OrderedDict()
	for zespol in Zespol.objects.all():
		statystyki[str(zespol)]=[zespol.rozegrane_spotkania(), zespol.wygrane_spotkania(), zespol.zremisowane_spotkania(), zespol.wygrane_spotkania()*3+zespol.zremisowane_spotkania()]
		print(statystyki[str(zespol)])

	statystyki_sorted = OrderedDict(sorted(statystyki.items(), key=lambda t: t[1][3], reverse=True))

	print(statystyki_sorted)

	return render(request, 'Mecze/tabela.html', {'statystyki': statystyki_sorted.items()})