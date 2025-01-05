from django.urls import path

from . import views
from . import views_cpu
from . import views_sound
from . import views_video

urlpatterns = [
	
	# With no path present, go to homepage
    path("", views.home, name="homepage"),
    
    path("cpu", views_cpu.home, name="cpu_home"),
    
    path("sound", views_sound.home, name="sound_home"),
    path("sound/device/<device_id>", views_sound.device, name="sound_device"),
    
    path("video", views_video.home, name="video_home"),
]