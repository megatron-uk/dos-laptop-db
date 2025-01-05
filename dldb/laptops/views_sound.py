from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """
	
	adriver = AudioDriver.objects.all()
	adigiother = AudioDigiOther.objects.all()
	adigisb = AudioDigiSB.objects.all()
	afm = AudioFM.objects.all()
	amidi = AudioMIDI.objects.all()
	aman = AudioManufacturer.objects.all()
	audio = Audio.objects.all().order_by('manufacturer__manufacturer', 'model')
	
	data = {
		'adriver' : adriver,
		'adigiother' : adigiother,
		'adigisb' : adigisb,
		'afm' : afm,
		'amidi' : amidi,
		'aman' : aman,
		'audio' : audio,
	}
	return render(request, "sound_homepage.html", data)
	
def device(request, device_id):
	""" Details of an audio device """
	
	audio = Audio.objects.get(pk = device_id)
	device_images = AudioImage.objects.filter(audio = audio)
	device_examples = AudioRecording.objects.filter(audio = audio)
	
	laptops = LaptopAudio.objects.filter(audio = audio)
	
	data = {
		'audio' : audio,
		'laptops' : laptops,
		'device_images' : device_images,
		'device_examples' : device_examples,
	}
	return render(request, "sound_device.html", data)