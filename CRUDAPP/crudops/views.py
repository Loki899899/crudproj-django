from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view (["POST",])
def IdealWeight(request):
	wei = ""
	print("that")
	try:
		if(request.method=="POST"):
			print("this")
			height=request.data.get('height')
			# height = 10
			weight=str(height*10)
			wei = weight
			return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
		if(request.method=="GET"):
			return JsonResponse("Ideal weight should be:"+wei+" kg",safe=False)
	except ValueError as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

# Create your views here.
