from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

# Create your views here.

def default_map(request):
	return render(request, 'default.html')


def send_data(request):
	data = json.loads(request.body)
	print(data)
	return JsonResponse(data)


def ramapi(request):
	# 9d411dc6b0e4cc020bd8b3b2e4ef69cc
	response = requests.get('https://randomuser.me/api/')

	data = json.loads(response.content)

	return JsonResponse(data)

