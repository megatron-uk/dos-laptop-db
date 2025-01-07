from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from .models import *

def home(request):
	""" Homepage """
	
	adriver = AudioDriver.objects.all()
	adigiother = AudioDigiOther.objects.all()
	adigisb = AudioDigiSB.objects.all()
	afm = AudioFM.objects.all()
	amidi = AudioMIDI.objects.all()
	aman = AudioManufacturer.objects.all().order_by('manufacturer')
	aman_count = Audio.objects.values('manufacturer__manufacturer', 'manufacturer__id').annotate(group_count=Count('id'))
	devices = Audio.objects.all().order_by('manufacturer__manufacturer', 'model')
	
	data = {
		'adriver' : adriver,
		'adigiother' : adigiother,
		'adigisb' : adigisb,
		'afm' : afm,
		'amidi' : amidi,
		'aman' : aman,
		'aman_count' : aman_count,
		'devices' : devices,
	}
	return render(request, "sound_homepage.html", data)
	
def company(request, company_id):
	""" Audio device company """
	
	aman = AudioManufacturer.objects.get(pk = company_id)
	devices = Audio.objects.filter(manufacturer = aman).order_by('model')
	audio_device_ids = []
	for a in devices:
		audio_device_ids.append(a.pk)
	laptops = LaptopAudio.objects.filter(audio__in = audio_device_ids).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	
	data = {
		'aman' : aman,
		'devices' : devices,
		'laptops' : laptops,
	}
	return render(request, "sound_company.html", data)
	
def device(request, device_id):
	""" Details of an audio device """
	
	audio = Audio.objects.get(pk = device_id)
	device_images = AudioImage.objects.filter(audio = audio)
	device_examples = AudioRecording.objects.filter(audio = audio)
	laptops = LaptopAudio.objects.filter(audio = audio).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	
	data = {
		'audio' : audio,
		'laptops' : laptops,
		'device_images' : device_images,
		'device_examples' : device_examples,
	}
	return render(request, "sound_device.html", data)
	
def sb_digi_device(request, device_support_id):
	
	device = AudioDigiSB.objects.get(pk = device_support_id)
	devices = Audio.objects.filter(digi_sb = device).order_by('manufacturer__manufacturer', 'model')
	audio_device_ids = []
	for a in devices:
		audio_device_ids.append(a.pk)
	laptops = LaptopAudio.objects.filter(audio__in = audio_device_ids).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	
	data = {
		'device' : device,
		'devices' : devices,
		'laptops' : laptops,
	}
	return render(request, "sound_sb_device.html", data)

def fm_device(request, device_support_id):
	
	device = AudioFM.objects.get(pk = device_support_id)
	devices = Audio.objects.filter(fm = device).order_by('manufacturer__manufacturer', 'model')
	audio_device_ids = []
	for a in devices:
		audio_device_ids.append(a.pk)
	laptops = LaptopAudio.objects.filter(audio__in = audio_device_ids).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	data = {
		'device' : device,
		'devices' : devices,
		'laptops' : laptops,
	}
	return render(request, "sound_fm_device.html", data)

def other_digi_device(request, device_support_id):
	
	device = AudioDigiOther.objects.get(pk = device_support_id)
	devices = Audio.objects.filter(digi_other = device).order_by('manufacturer__manufacturer', 'model')
	audio_device_ids = []
	for a in devices:
		audio_device_ids.append(a.pk)
	laptops = LaptopAudio.objects.filter(audio__in = audio_device_ids).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	data = {
		'device' : device,
		'devices' : devices,
		'laptops' : laptops,
	}
	return render(request, "sound_other_digi_device.html", data)

def midi_device(request, device_support_id):
	
	device = AudioMIDI.objects.get(pk = device_support_id)
	devices = Audio.objects.filter(midi = device).order_by('manufacturer__manufacturer', 'model')
	audio_device_ids = []
	for a in devices:
		audio_device_ids.append(a.pk)
	laptops = LaptopAudio.objects.filter(audio__in = audio_device_ids).order_by('laptop__manufacturer__manufacturer', 'laptop__model', 'laptop__submodel')
	data = {
		'device' : device,
		'devices' : devices,
		'laptops' : laptops,
	}
	return render(request, "sound_midi_device.html", data)