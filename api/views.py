from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def index(request):
  result = [1, 2, 3]
  return JsonResponse(result, safe=False)