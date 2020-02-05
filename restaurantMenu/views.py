# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from django.shortcuts import render

# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# @ensure_csrf_cookie
# @csrf_exempt
def index(request):
	if request.method == 'POST':
		print("POST Request")
		print(request.path)
		print(request.content_type)
		print(request.method)
		# print(request.META)
		print(request.content_params)

	if request.method == 'PUT':
		print("Put Request")
		print(request.path)
		print(request.content_type)
		print(request.method)
		# print(request.META)
		print(request.content_params)	# question_list = Question.objects.order_by('-pub_date')[:5]
	return render(request,"restaurantMenu/index.html",{"name":"Chanikya","city":"Bangalore"})
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