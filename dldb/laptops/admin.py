from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Audio)
admin.site.register(AudioManufacturer)
admin.site.register(AudioDigiOther)
admin.site.register(AudioDigiSB)
admin.site.register(AudioDriver)
admin.site.register(AudioFM)
admin.site.register(AudioImage)
admin.site.register(AudioMIDI)
admin.site.register(AudioRecording)
admin.site.register(Bus)
admin.site.register(Chipset)
admin.site.register(CPUClass)
admin.site.register(Laptop)
admin.site.register(LaptopManufacturer)
admin.site.register(LaptopAudio)
admin.site.register(LaptopCPU)
admin.site.register(LaptopImage)
admin.site.register(LaptopVideo)
admin.site.register(LaptopLCD)
admin.site.register(LCD)
admin.site.register(LCDType)
admin.site.register(Mouse)
admin.site.register(RamType)
admin.site.register(ScalingImage)
admin.site.register(Video)
admin.site.register(VideoManufacturer)
admin.site.register(VideoAccel)
admin.site.register(VideoAccel3DTypes)
admin.site.register(VideoImage)
admin.site.register(VideoScalingHW)
admin.site.register(VideoScalingSW)



