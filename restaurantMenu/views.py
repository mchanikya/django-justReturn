# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from django.shortcuts import render

# Create your views here.
def index(request):
	# question_list = Question.objects.order_by('-pub_date')[:5]
	return render(request,"restaurantMenu/index.html")
	# pass

def getJson(request):
	data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
	# question_list = Question.objects.order_by('-pub_date')[:5]
	return JsonResponse(data)
	# pass

def getString(request):
	print("In getString")
	return JsonResponse({"tag":"Welcome to django strings"})