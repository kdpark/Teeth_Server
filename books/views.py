from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404
from books.models import Publisher

def showbook(request):
	#return render_to_response()
