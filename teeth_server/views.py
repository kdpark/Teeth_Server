from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse

def home(request):

	return HttpResponse("Hello, This is Teeth!!")

def temp(request):
	
	data = {}
	todos = [ {'title': 'Mow the lawn', 'importance': 'Minor'},
	        {'title': 'Backup your PC', 'importance': 'High'},
	        {'title': 'Buy some Milk', 'importance': 'Medium'}, ]
	data['todos'] = todos
	return render_to_response("index.html", data, context_instance=RequestContext(request))
