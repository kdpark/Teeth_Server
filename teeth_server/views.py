from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth, admin
import json

def home(request):
	return HttpResponse("Hello, This is Teeth!!")

def search_form(request):
	return render_to_response('search_form.html')

"""
@csrf_exempt
def search(request):
	if 'first' in request.POST and request.POST['first']:
		q = request.POST['first']
		books = Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html', {'books': books, 'query': q})
	else:
		return render_to_response('search_form.html', {'error': True})
"""

def login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/accounts/loggedin/")
	else:
        # Show an error page
		return HttpResponseRedirect("/accounts/invalid/")

def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/accounts/loggedout/")

def example(request):
	# json example
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	if(username == 'abc' and password =='123'):
		status = 1
		log = 'success'
	else:
		status = 2
		log = 'failed'

	c = {'Status' : status, 'Log':log}
	output = json.dumps(c, indent=4, separators = (',', ':'))
	return HttpResponse(output)

def main(request):
	# input : user id.
	# output : c_person name, c_person pic, target_id
	# main function, ? , view connection person
	# random my friend
	# and random his other gender friend
	return 1

def open(request):
	#
	return 1
