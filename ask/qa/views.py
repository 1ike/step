#from django.http import HttpResponse
from django.shortcuts import render_to_response

def test(request, *args, **kwargs):


  return render_to_response('h.html')
#  return HttpResponse('OK')