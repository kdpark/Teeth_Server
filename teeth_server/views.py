from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404
import datetime

def home(request):
	return HttpResponse("Hello, This is Teeth!!")

def current_datetime(request):
	data = {}
	now = datetime.datetime.now()
	data['now'] = now
	return render_to_response("index.html", data, context_instance=RequestContext(request))

def hour_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	if (offset>99):
		raise Http404()

	#assert False

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hours, it will be %s.<body></html>" % (offset, dt)
	return HttpResponse(html)

def temp(request):
	data = {}
	todos = [ {'title': 'Mow the lawn', 'importance': 'Minor'},
	        {'title': 'Backup your PC', 'importance': 'High'},
	        {'title': 'Buy some Milk', 'importance': 'Medium'}, ]
	data['todos'] = todos
	return render_to_response("index.html", data, context_instance=RequestContext(request))
