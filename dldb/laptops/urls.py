from django.urls import path

from . import views
from . import views_cpu
from . import views_sound
from . import views_video

urlpatterns = [
	
	# With no path present, go to homepage
    path("", views.home, name="homepage"),
    
    path("cpu", views_cpu.home, name="cpu_home"),
    path("cpu/cpu/<device_id>", views_cpu.cpu_device, name="cpu_device"),
    path("cpu/chipset/<device_id>", views_cpu.chipset_device, name="chipset_device"),
    
    path("sound", views_sound.home, name="sound_home"),
    path("sound/device/<device_id>", views_sound.device, name="sound_device"),
    path("sound/sb/<device_support_id>", views_sound.sb_digi_device, name="sb_digi_device"),
    path("sound/digi/<device_support_id>", views_sound.other_digi_device, name="other_digi_device"),
    path("sound/fm/<device_support_id>", views_sound.fm_device, name="fm_device"),
    path("sound/midi/<device_support_id>", views_sound.midi_device, name="midi_device"),
    
    path("video", views_video.home, name="video_home"),
]