from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """

	laptops = Laptop.objects.all()
	
	# Latest laptops
	latest_laptops = laptops
	if latest_laptops:
		latest_laptops = latest_laptops[0:5]
		latest_laptops.reverse()
	
	# Group by manufacturer
	laptops_mfr_groupby = laptops.values('manufacturer__manufacturer').annotate(group_count=Count('id')).order_by('group_count')
	
	# Group by model
	laptops_model_groupby = laptops.values('model').annotate(group_count=Count('id')).order_by('group_count')
	
	# Group by submodel
	laptops_submodel_groupby = laptops.values('submodel').annotate(group_count=Count('id')).order_by('group_count')
	
	# Most common laptop manufacturer
	laptops_mfr_highest = None
	if laptops_mfr_groupby:
		laptops_mfr_highest = laptops_mfr_groupby.last()
		
	# Most common laptop model
	laptops_model_highest = None
	if laptops_model_groupby:
		laptops_model_highest = laptops_model_groupby.last()
	
	data = {
		
		'laptops' : laptops,
		'laptops_mfr_groupby' : laptops_mfr_groupby,
		'laptops_mfr_highest' : laptops_mfr_highest,
		'laptops_model_groupby' : laptops_model_groupby,
		'laptops_submodel_groupby' : laptops_submodel_groupby,
		'laptops_model_highest' : laptops_model_highest,
		'latest_laptops' : latest_laptops,
	}
		
	return render(request, "laptop_homepage.html", data)
	
def device(request, device_id):
	""" A laptop """
	
	laptop = Laptop.objects.get(pk = device_id)
	
	laptopcpu = LaptopCPU.objects.filter(laptop = laptop)
	laptopaudio = LaptopAudio.objects.filter(laptop = laptop)
	laptopvideo = LaptopVideo.objects.filter(laptop = laptop)
	laptoplcd = LaptopLCD.objects.filter(laptop = laptop)
	laptopimages = LaptopImage.objects.filter(laptop = laptop)
	
	data = {
		'laptop' : laptop,	
		'laptopcpu' : laptopcpu,
		'laptopaudio' : laptopaudio,
		'laptopvideo' : laptopvideo,
		'laptoplcd' : laptoplcd,
		'laptopimages' : laptopimages,
	}
	
	return render(request, "laptop_device.html", data)