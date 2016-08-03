from django.shortcuts import get_object_or_404, render_to_response

from django.template import loader, RequestContext
from rest_framework import viewsets
from users.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from django.conf import settings

def home(request):
  return render_to_response('flavoUr/landing.html', context_instance=RequestContext(request))
