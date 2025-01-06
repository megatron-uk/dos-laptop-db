from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """
	
	chipset = Chipset.objects.all().order_by('name')
	cpuclass = CPUClass.objects.all().order_by('name')
	
	data = {
		'chipset' : chipset,
		'cpuclass' : cpuclass,
	}
	return render(request, "cpu_homepage.html", data)
	
def cpu_device(request, device_id):
	""" 486DX """
	cpu = CPUClass.objects.get(pk = device_id)
	laptops = LaptopCPU.objects.filter(cpu = cpu)
	data = {
		'cpu' : cpu,
		'laptops' : laptops,
	}
	return render(request, "cpu_cpu_device.html", data)

def chipset_device(request, device_id):
	""" Intel 440BX """
	chipset = Chipset.objects.get(pk = device_id)
	laptops = Laptop.objects.filter(chipset = chipset)
	data = {
		'chipset' : chipset,
		'laptops' : laptops,
	}
	return render(request, "cpu_chipset_device.html", data)