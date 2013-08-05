from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth, admin
from meeting.models import User
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
def simpleJson(num, msg):
	c = {'Status' : num, 'Log': msg}
	return json.dumps(c, indent=4, separators = (',', ':'))

def login(request):
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	
	if (email=='' or password==''):
		return HttpResponse(simpleJson(4,'Error-Blank Form'))

	target = User.objects.filter(email__exact=email)
	if target.count():
		#existing
		if target[0].password == password:
			c = {'Status' : 1, 'Log': 'success', 'Value': target[0].id}
			return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))
		else:
			return HttpResponse(simpleJson(2, 'Wrong password'))
	else:
		return HttpResponse(simpleJson(3, 'The email is not in DB'))

def signin(request):
	# join module, Create User
	# POST : username, email, password
	# OUTPUT : 1- success, 2- duplicated email, 3-blank form
	email = request.POST.get('email','')
	username = request.POST.get('username','')
	password = request.POST.get('password','')

	if (email=='' or username=='' or password==''):
		return HttpResponse(simpleJson(3,'Error-Blank Form'))

	if User.objects.filter(email__exact=email).count():
		return HttpResponse(simpleJson(2, 'Duplicated Email'))

	newUser = User(name=username, password=password, email=email)
	newUser.save()
	return HttpResponse(simpleJson(1, 'Success sign'))

def example(request):
	# json example
	username = request.POST.get('username')
	password = request.POST.get('password')
	if(username == 'abc' and password =='123'):
		status = 1
		log = 'success'
	else:
		status = 2
		log = 'failed'

	return HttpResponse(simpleJson(status, log))

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
