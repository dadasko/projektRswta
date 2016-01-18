from django.contrib import admin
from .models import Zespol
from .models import Zawodnik
from .models import Pozycja
from .models import Sklad
from .models import Kolejka
from .models import Mecz
from .models import Bramka
from django import forms


class MeczAdmin(admin.ModelAdmin):
	model = Mecz

	search_fields = ('gospodarz__nazwa', 'gosc__nazwa')

	list_filter = ('kolejka__nr_kolejki',)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		# str = "/Mecze/mecz/strona/1/"
		str = request.path
		found = [int(s) for s in str.split("/") if s.isdigit()]
		if db_field.name == 'sklad_gospodarza':
			print(Sklad.objects.filter(zespol=Mecz.objects.filter(pk=found[0])[0].gospodarz))
			kwargs['queryset'] = Sklad.objects.filter(zespol=Mecz.objects.filter(pk=found[0])[0].gospodarz)

		if db_field.name == 'sklad_goscia':
			kwargs['queryset'] = Sklad.objects.filter(zespol=Mecz.objects.filter(pk=found[0])[0].gosc)

		return super(MeczAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['gospodarz', 'gosc', ]
		else:
			return ['sklad_gospodarza', 'sklad_goscia']


class SkladAdmin(admin.ModelAdmin):
	model = Sklad

	list_filter = ('zespol',)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		# str = "/Mecze/mecz/strona/1/"

		# print(str)
		# print(found[0])
		# print(request.path)
		if db_field.name.startswith('zawodnik'):
			str = request.path
			found = [int(s) for s in str.split("/") if s.isdigit()]
			# print(Sklad.objects.filter(zespol=Mecz.objects.filter(pk=found[0])[0].gospodarz))
			kwargs['queryset'] = Zawodnik.objects.filter(zespol=Sklad.objects.filter(pk=found[0])[0].zespol)
		#
		# if db_field.name == 'sklad_goscia':
		# 	kwargs['queryset'] = Sklad.objects.filter(zespol=Mecz.objects.filter(pk=found[0])[0].gosc)

		return super(SkladAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['zespol', ]
		else:
			return ['zawodnik_1', 'pozycja_1',
					'zawodnik_2', 'pozycja_2',
					'zawodnik_3', 'pozycja_3',
					'zawodnik_4', 'pozycja_4',
					'zawodnik_5', 'pozycja_5',
					'zawodnik_6', 'pozycja_6',
					'zawodnik_7', 'pozycja_7',
					'zawodnik_8', 'pozycja_8',
					'zawodnik_9', 'pozycja_9',
					'zawodnik_10', 'pozycja_10',
					'zawodnik_11', 'pozycja_11']


class ZawodnikAdmin(admin.ModelAdmin):
	list_filter = ('zespol',)
	search_fields = ('imie', 'nazwisko')


class ZespolAdmin(admin.ModelAdmin):
	search_fields = ('nazwa',)


# Register your models here.
admin.site.register(Zespol, ZespolAdmin)
admin.site.register(Zawodnik, ZawodnikAdmin)
admin.site.register(Pozycja)
admin.site.register(Sklad, SkladAdmin)
admin.site.register(Kolejka)
admin.site.register(Mecz, MeczAdmin)
admin.site.register(Bramka)
