from django.urls import path

from . import views
from . import views_cpu
from . import views_sound
from . import views_video
from . import views_lcd
from . import views_laptop

urlpatterns = [
	
	# With no path present, go to homepage
    path("", views.home, name="homepage"),
    
    # CPU and chipset
    path("cpu", views_cpu.home, name="cpu_home"),
    path("cpu/cpu/<device_id>", views_cpu.cpu_device, name="cpu_device"),
    path("cpu/chipset/<device_id>", views_cpu.chipset_device, name="chipset_device"),
    
    # Audio
    path("sound", views_sound.home, name="sound_home"),
    path("sound/company/<company_id>", views_sound.company, name="sound_company"),
    path("sound/device/<device_id>", views_sound.device, name="sound_device"),
    path("sound/sb/<device_support_id>", views_sound.sb_digi_device, name="sb_digi_device"),
    path("sound/digi/<device_support_id>", views_sound.other_digi_device, name="other_digi_device"),
    path("sound/fm/<device_support_id>", views_sound.fm_device, name="fm_device"),
    path("sound/midi/<device_support_id>", views_sound.midi_device, name="midi_device"),
    
    # Graphics
    path("video", views_video.home, name="video_home"),
    
    # LCD panels
    path("screen", views_lcd.home, name="lcd_home"),
    
    # Laptops
    path("laptop", views_laptop.home, name="laptop_home"),
    path("laptop/device/<device_id>", views_laptop.device, name="laptop_device"),
]