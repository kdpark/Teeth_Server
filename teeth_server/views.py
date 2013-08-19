from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth, admin
from meeting.models import User
import json
import random

def home(request):
  return HttpResponse("Hello, This is Teeth!!")

def search_form(request):
  return render_to_response('search_form.html')

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
  option = request.POST.get('opt', '')
  email = request.POST.get('email','')
  username = request.POST.get('username','')
  password = request.POST.get('password','')
  gender = request.POST.get('gender', '')
  fb_id = request.POST.get('fb_id', '')
  fb_friend = request.POST.get('fb_friend','')
  phone_num = request.POST.get('phone_num', '')

  if option == '1': # normal sign in
    if (email=='' or username=='' or password=='' or gender=='' or phone_num==''):
      return HttpResponse(simpleJson(3,'Error-Blank Form'))

  elif option =='2': # facebook sign in
    if (email=='' or username=='' or password=='' or gender=='' or fb_id==''):
      return HttpResponse(simpleJson(3,'Error-Blank Form'))
  else:
    return HttpResponse(simpleJson(4, 'check your options'))

  if User.objects.filter(email__exact=email).count():
    return HttpResponse(simpleJson(2, 'Duplicated Email'))
  
  newUser = User(name=username, password=password, email=email, gender=gender, fb_id=fb_id, phone_num=phone_num)
  newUser.save()

  if fb_friend != '':
    # friend add from facebook's friend
    pass
  return HttpResponse(simpleJson(1, 'Success sign'))

  

def main(request):
  # input : user id.
  # output : arranger_name, next_arranger_name, candidate_num

  email = request.POST.get('email', '')
  password = request.POST.get('password', '')

  try:
    user = User.objects.get(email__exact=email, password__exact=password)
  except DoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  # if friend_num is under 5...
  friend_num = User.objects.filter(friend_ship=user.id).count()
  if friend_num < 3:
    c = {'Status' : 3, 'Log': 'You need more friends', 'Value': friend_num}
    return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))

  # already use chance
  if user.chance ==2:
    return HttpResponse(simpleJson(4, 'You have no more chance'))

  try: # is there arranger ?
    arranger_now = User.objects.get(id=user.arranger_now.id)
    
  except DoesNotExist: # there is no arranger info
    get_new_target(request)
    pass

  c = {
        'Status' : 1, 'Log': 'success', \
        'arranger_now': user.arranger_now.name, 'arranger_now_pic': user.arranger_now.profile_pic, \
        'candidate_now': user.candidate_now.name, 'candidate_now_pic': user.candidate_now.profile_pic, \
        'candidate_num': user.candidate_num
      }
  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))
  

def get_new_target(request):

  # if arranger blank:
    # pick random my friend
    # save him to arranger
    # pick random his other gender friend
    # save her to candidate

  # else arranger on:
  email = request.POST.get('email', '')
  password = request.POST.get('password', '')

  try:
    user = User.objects.get(email__exact=email, password__exact=password)
  except DoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  friend_list = User.objects.filter(friend_ship=user.id)

  # upgrade plan :: search friend_list, which has one more friend with target_gender
  # upgrade plan :: and then, select one as arranger, then, select his friend as candidate

  target_gender = 1
  if user.gender ==1:
    target_gender = 2

  output = []
  for friend in friend_list:
    output += User.objects.filter(friend_ship=friend.id, gender=target_gender).exclude(friend_ship=user.id)

  # remove duplicate
  output = list(set(output))
  candidate_num = len(output)

  # no candidate!
  if candidate_num == 0:
    return HttpResponse(simpleJson(4, 'No candidate...'))

  # finding an arranger !
  candidate = random.sample(output,1)[0]
  candidate_friend_list = User.objects.filter(friend_ship=candidate.id)
  arranger = random.sample(list(set(friend_list).intersection(set(candidate_friend_list))), 1)[0]

  user.candidate_now = candidate
  user.arranger_now = arranger
  user.candidate_num = candidate_num
  user.save()
  return 1


def add_friend(request):
  # auto add using facebook or phone_num (sync)

  # manually request
  email = request.POST.get('email', '')
  password = request.POST.get('password', '')
  target_email = request.POST.get('target','')
  
  if target_email == '':
    HttpResponse(simpleJson(3, 'no target friend'))

  try:
    user = User.objects.get(email__exact=email, password__exact=password)
  except DoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  target_friend = User.objects.get(email=target_email)
  user.friend_ship.add(target_friend)

  return HttpResponse(simpleJson(1, 'success'))

def pick_candidate(request):
  # get her number
  # and turn the chance OFF

  email = request.POST.get('email', '')
  password = request.POST.get('password', '')

  try:
    user = User.objects.get(email__exact=email, password__exact=password)
  except DoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  c = {
        'Status' : 1, 'Log': 'success', \
        'candidate_phone': user.candidate_now.phone_num, 'candidate_pic': user.candidate_now.profile_pic
      }
  user.chance = 2
  user.save()

  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))

def new_cycle(request):
  # this funtion will only used by admin
  # Turn all chance ON
  # And all user, get new arranger & candidate

  email = request.POST.get('adminid', '')
  password = request.POST.get('password', '')

  if email=='teeth' and password=='xltm0630@':
    return HttpResponse(simpleJson(2, 'access deny'))

  for user in User.objects.all():
    user.chance = 1
    user.save()

    # if friend_num is under 5... pass
    friend_num = User.objects.filter(friend_ship=user.id).count()
    if friend_num < 3:
      continue
    
    friend_list = User.objects.filter(friend_ship=user.id)

    # upgrade plan :: search friend_list, which has one more friend with target_gender
    # upgrade plan :: and then, select one as arranger, then, select his friend as candidate

    target_gender = 1
    if user.gender == 1:
      target_gender = 2

    output = []
    for friend in friend_list:
      output += User.objects.filter(friend_ship=friend.id, gender=target_gender).exclude(friend_ship=user.id)

    # remove duplicate
    output = list(set(output))
    candidate_num = len(output)

    # no candidate!
    if candidate_num == 0:
      user.candidate_num =0
      user.save()
      continue

    # finding an arranger !
    candidate = random.sample(output,1)[0]
    candidate_friend_list = User.objects.filter(friend_ship=candidate.id)
    arranger = random.sample(list(set(friend_list).intersection(set(candidate_friend_list))), 1)[0]

    user.candidate_now = candidate
    user.arranger_now = arranger
    user.candidate_num = candidate_num
    #

    user.save()

  # done
  return HttpResponse(simpleJson(1, 'success new cycle'))












