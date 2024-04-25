
from django.shortcuts import render
from math import *
# from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def submitquery(request):
  query = request.GET['query']
  try:
    answer = round(eval(query), 2)
    error = False
    # queryDict = {
    #   'Query' : query,
    #   'Answer': answer,
    #   'error' : False
    # }
    return render(request, 'index.html',{"answer":answer})
  except:
    error  = True
    error = 'error'
    return render(request, 'index.html',{"error":error})
