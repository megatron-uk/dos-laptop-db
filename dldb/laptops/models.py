from django.db import models

class AudioDriver(models.Model):
	""" No driver, one time init, loadable driver, tsr, etc """

	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Driver"

class AudioDigiOther(models.Model):
	""" WSS etc"""
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Digi Other Support"

class AudioDigiSB(models.Model):
	""" SB, SB Pro, SB 16 """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Digi SB Support"
	
class AudioFM(models.Model):
	""" OPL2, ESFM, Emulated OPL3 etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio FM Support"
	
class AudioMIDI(models.Model):
	""" MPU401 etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio MIDI Support"
	
class Bus(models.Model):
	""" ISA, PCI, etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name} interface" 
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Bus Interface"

# Create your models here.
class Audio(models.Model):
	""" A soundcard """
	
	manufacturer = models.CharField(max_length = 255, unique = False, blank = False)
	model = models.CharField(max_length = 255, unique = True, blank = False)
	bus = models.ForeignKey(Bus, on_delete=models.PROTECT)
	digi_sb = models.ForeignKey(AudioDigiSB, on_delete=models.PROTECT)
	digi_other = models.ForeignKey(AudioDigiOther, on_delete=models.PROTECT)
	fm = models.ForeignKey(AudioFM, on_delete=models.PROTECT)
	midi = models.ForeignKey(AudioMIDI, on_delete=models.PROTECT)
	driver = models.ForeignKey(AudioDriver, on_delete=models.PROTECT)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return f"{self.manufacturer} {self.model}" 
	
	class Meta:
		verbose_name_plural = "Audio Cards"

class Chipset(models.Model):
	""" Intel 440BX """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)

	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Chipsets"

class CPUClass(models.Model):
	""" Intel Pentium """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)

	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "CPU Types"

class LCDType(models.Model):
	""" TFT, DSTN """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)

	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "LCD Types"

class LCD(models.Model):
	
	res_x = models.IntegerField(blank = False)
	res_y = models.IntegerField(blank = False)
	screen_size = models.FloatField(blank = False)
	screen_type = models.ForeignKey(LCDType, on_delete=models.PROTECT)
	
	def __str__(self):
		return f'{self.res_x}x{self.yes_y}, {self.screen_size}" ({self.screen_type.name})' 
	
	class Meta:
		verbose_name_plural = "LCD Screen Models"

class Mouse(models.Model):
	""" Trackpad, Trackpoint, Trackball, None, etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Mouse/Pointer Types"

class RamType(models.Model):
	""" PC66, PC100 """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)

	def __str__(self):
		return f"{self.name} RAM" 
	
	class Meta:
		verbose_name_plural = "RAM Types"

class VideoAccel3DTypes(models.Model):
	""" OpenGL, S3D, Glige, Direct3D """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Video 3D Accleration Types"

class VideoScalingHW(models.Model):
	""" No scaling in hw, bilinear, etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Video Scaling (HW)"

class VideoScalingSW(models.Model):
	""" No scaling software, driver, TSE """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Video Scaling (HW)"

class Video(models.Model):
	""" A videocard """
	
	manufacturer = models.CharField(max_length = 255, unique = False, blank = False)
	model = models.CharField(max_length = 255, unique = True, blank = False)
	bus = models.ForeignKey(Bus, on_delete=models.PROTECT)
	ram = models.FloatField(default = 0, blank = False)
	scaling_hw = models.ForeignKey(VideoScalingHW, on_delete=models.PROTECT)
	scaling_sw = models.ForeignKey(VideoScalingSW, on_delete=models.PROTECT)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return f"{self.manufacturer} {self.model} ({self.ram} MB)"
	
	class Meta:
		verbose_name_plural = "Video Cards"

class VideoAccel(models.Model):
	""" Types of 3D acceleration a videocard can have """
	
	video = models.ForeignKey(Video, on_delete=models.PROTECT) 
	accel3d = models.ForeignKey(VideoAccel3DTypes, on_delete=models.PROTECT) 
	
	class Meta:
		constraints = [
			models.UniqueConstraint(			# A card can only have 'opengl' once.
				fields=["video", "accel3d"],
				name="unique_video_accel"
			)
		]
		verbose_name_plural = "Video Card Capabilities"
		
	def __str__(self):
		return f"{self.video.manufacturer} {self.video.model} ({self.video.ram} MB) - {self.accel3d.name}"

class Laptop(models.Model):
	"""IBM Thinkpad 385ED """
	
	manufacturer = models.CharField(max_length = 255, unique = False, blank = False)
	model = models.CharField(max_length = 255, unique = False, blank = False)
	submodel = models.CharField(max_length = 255, unique = False, blank = False)
	chipset = models.ForeignKey(Chipset, on_delete=models.PROTECT)
	cpu = models.ForeignKey(CPUClass, on_delete=models.PROTECT)
	cpumin = models.IntegerField(default=0, blank=False)
	cpumax = models.IntegerField(default=0, blank=False)
	ram = models.ForeignKey(RamType, on_delete=models.PROTECT)
	ramslots = models.IntegerField(default=0, blank=False)
	rammin = models.IntegerField(default=0, blank=False)
	rammax = models.IntegerField(default=0, blank=False)
	lcd = models.ForeignKey(LCD, on_delete=models.PROTECT)
	video = models.ForeignKey(Video, on_delete=models.PROTECT)
	audio = models.ForeignKey(Audio, on_delete=models.PROTECT)
	audio_out = models.BooleanField(default = False)
	line_in = models.BooleanField(default = False)
	mic_in = models.BooleanField(default = False)
	pcmcia = models.IntegerField(default = 0, blank=False)
	mouse = models.ForeignKey(Mouse, on_delete=models.PROTECT)
	
	def __str__(self):
		return f"{self.manufacturer} {self.model} {self.submodel} ({self.lcd}))"
	
	class Meta:
		constraints = [
			models.UniqueConstraint(	
				fields=["manufacturer", "model", "submodel", "lcd"],
				name="unique_laptop"
			)
		]
		verbose_name_plural = "Laptops"

class LaptopAudio(models.Model):
	
	laptop = models.ForeignKey(Laptop, on_delete=models.PROTECT)
	audio = models.ForeignKey(Audio, on_delete=models.PROTECT)
	
	def __str__(self):
		return f"{self.laptop} - {self.audio})"
	
	class Meta:
		constraints = [
			models.UniqueConstraint(	
				fields=["laptop", "audio"],
				name="unique_laptop_audio"
			)
		]
		verbose_name_plural = "Laptop Audio"