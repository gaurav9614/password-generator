from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def password(request):
	thePassword = ''
	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length'))
	
	if request.GET.get('Uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('Numbers'):
		characters.extend(list('0123456789'))
	if request.GET.get('Special'):
		characters.extend(list('~!@#$%^&*()'))
	
	for i in range(length):
		thePassword += random.choice(characters)
	return render(request,'generator/password.html', {'password':thePassword})

def about(request):
	return render(request, 'generator/about.html')