from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """

	screentypes = LCDType.objects.all().order_by('name')
	screens = LCD.objects.all().order_by('screen_type__name', 'screen_size', 'res_x', 'res_y')
	
	data = {
		'screentypes' : screentypes,
		'screens' : screens,
	}
	return render(request, "lcd_homepage.html", data)
	