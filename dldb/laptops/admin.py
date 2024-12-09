from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AudioDriver)
admin.site.register(AudioFM)
admin.site.register(AudioDigiSB)
admin.site.register(AudioDigiOther)
admin.site.register(AudioMIDI)
admin.site.register(Bus)
admin.site.register(VideoScalingHW)
admin.site.register(VideoScalingSW)
admin.site.register(VideoAccel3DTypes)
admin.site.register(Audio)
admin.site.register(Video)
