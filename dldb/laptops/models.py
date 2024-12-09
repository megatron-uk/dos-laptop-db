from django.db import models

# Create your models here.

class AudioDriver(models.Model):
	""" No driver, one time init, loadable driver, tsr, etc """

	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Driver"
	
class AudioFM(models.Model):
	""" OPL2, ESFM, Emulated OPL3 etc """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio FM Support"

class AudioDigiSB(models.Model):
	""" SB, SB Pro, SB 16 """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Digi SB Support"
	
class AudioDigiOther(models.Model):
	""" WSS etc"""
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Audio Digi Other Support"
	
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
		verbose_name_plural = "Video Scaling (SW)"
	
class VideoAccel3DTypes(models.Model):
	""" OpenGL, S3D, Glige, Direct3D """
	
	name = models.CharField(max_length = 255, unique = True, blank = False)
	
	def __str__(self):
		return f"{self.name}" 
	
	class Meta:
		verbose_name_plural = "Video 3D Accleration Types"
	
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