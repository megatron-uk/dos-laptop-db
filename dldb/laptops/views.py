from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """
	
	laptops = Laptop.objects.all()
	laptops_count = laptops.count()
	laptops_mfr_count = Laptop.objects.values('manufacturer__manufacturer').distinct().count()
	
	# Most common laptop manufacturer
	laptops_mfr_groupby = laptops.values('manufacturer__manufacturer').annotate(group_count=Count('id'))
	laptops_mfr_highest = None
	if laptops_mfr_groupby:
		laptops_mfr_highest = laptops_mfr_groupby[0]
		
	# Most common laptop model
	laptops_model_groupby = laptops.values('model').annotate(group_count=Count('id'))
	laptops_model_highest = None
	if laptops_model_groupby:
		laptops_model_highest = laptops_model_groupby[0]	
	
	#################################
	
	video = Video.objects.all()
	video_count = video.count()
	video_mfr_count = Video.objects.values('manufacturer__manufacturer').distinct().count()
	
	# Most common video manufacturer 
	video_mfr_groupby = video.values('manufacturer__manufacturer').annotate(group_count=Count('id'))
	video_mfr_highest = None
	if video_mfr_groupby:
		video_mfr_highest = video_mfr_highest[0]
	
	#################################
	
	audio = Audio.objects.all()
	audio_count = audio.count()
	audio_mfr_count = Audio.objects.values('manufacturer__manufacturer').distinct().count()
	
	# Most common audio manufacturer 
	audio_mfr_groupby = audio.values('manufacturer__manufacturer').annotate(group_count=Count('id'))
	audio_mfr_highest = None
	if audio_mfr_groupby:
		audio_mfr_highest = audio_mfr_groupby[0]
	
	#################################
	
	screens = LCD.objects.all()
	screen_count = screens.count()
	
	# Most common screen size
	screen_size_count = screens.values('screen_size').annotate(group_count=Count('id'))
	screen_size_count.reverse()
	screen_size_highest = None
	if screen_size_count:
		screen_size_highest = screen_size_count[0]
		
	# Most common screen type
	screen_type_count = screens.values('screen_type__name').annotate(group_count=Count('id'))
	screen_type_count.reverse()
	screen_type_highest = None
	if screen_type_count:
		screen_type_highest = screen_type_count[0]
		
	# Most common screen res - this is a bit hacky,,,
	screen_res_highest = None
	screen_res_modes = {}
	for s in screens:
		res_mode = f"{s.res_x}x{s.res_y}"
		if res_mode in screen_res_modes:
			screen_res_modes[res_mode] += 1
		else:
			screen_res_modes[res_mode] = 1
	sorted_res_modes = sorted(screen_res_modes.items(), key=lambda item: item[1])
	sorted_res_modes.reverse()
	if sorted_res_modes:
		screen_res_highest = sorted_res_modes[0]
		
	data = {
		'laptops_count' : laptops_count,
		'laptops_mfr_count' : laptops_mfr_count,
		'laptops_mfr_highest' : laptops_mfr_highest,
		'laptops_model_highest' :laptops_model_highest,
		
		'audio_count' : audio_count,
		'audio_mfr_count' : audio_mfr_count,
		'audio_mfr_highest' : audio_mfr_highest,
		
		'video_count' : video_count,
		'video_mfr_count' : video_mfr_count,
		'video_mfr_highest' : video_mfr_highest,
		
		'screen_count' : screen_count,
		'screen_size_highest' : screen_size_highest,
		'screen_type_highest' : screen_type_highest,
		'screen_res_highest' : screen_res_highest,
	}
	return render(request, "homepage.html", data)