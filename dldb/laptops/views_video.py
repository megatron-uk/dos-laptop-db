from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
	""" Homepage """
	
	data = {
	}
	return render(request, "video_homepage.html", data)