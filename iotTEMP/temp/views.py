# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

from django.template import loader
from .models import TempData
from random import randint

#  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
#  UNI:   mh3895,  xz2754,  yw3225
#  Group Code: MOHA

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world.")

import boto3
import mraa
from time import sleep
from math import log

button_pin = 4
button = mraa.Gpio(button_pin)
button.dir(mraa.DIR_IN)
tempSensor = mraa.Aio(0)

def getcelcius(value):
	B = 4275.0
	R0 = 100000.0
	R = 1023.0/value - 1.0
	R *= R0
	temp = 1.0 / (log(R / R0)/B + 1.0/298.15) - 273.15
	return temp

def index(request):
    # Datalist = TempData.objects.all()
	context = {}
	# if button.read() == 1:
	# test = getcelcius(tempSensor.read())
	test = []
	for i in range(20):
		# test0 = randint(0, 9)
		test0 = getcelcius(tempSensor.read())
		test.append(test0)
		sleep(0.5)
	Edisonlist = {}
	Edisonlist = {'gettemp': test}
	context = {'Edisonlist': Edisonlist}
	
	return render(request, 'temp/index.html', context)

