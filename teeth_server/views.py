from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth, admin
from django.db import connection
from meeting.models import User
import json
import random

def home(request):
  return HttpResponse("Hello, This is Teeth!!")

def simpleJson(num, msg):
  c = {'Status' : num, 'Log': msg}
  return json.dumps(c, indent=4, separators = (',', ':'))


def login(request):
  email = request.POST.get('email', '')
  password = request.POST.get('password', '')
  
  if (email=='' or password==''):
    return HttpResponse(simpleJson(4,'Error-Blank Form'))
  
  try:
    target = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(3, 'The email is not in DB'))
  
  if target.password == password:
    c = {'Status' : 1, 'Log': 'success', 'Value': target.id}
    return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))
  else:
    return HttpResponse(simpleJson(2, 'Wrong password'))
  

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
  fb_email = request.POST.get('fb_email','')
  phone_contact = request.POST.get('phone_contact', '')
  phone_num = request.POST.get('phone_num', '')

  if option == '1': # normal sign in
    if (email=='' or username=='' or password=='' or gender=='' or phone_num==''):
      return HttpResponse(simpleJson(3,'Error-Blank Form'))
    if User.objects.filter(email__exact=email).count():
      return HttpResponse(simpleJson(2, 'Duplicated Email'))

    newUser = User(name=username, password=password, email=email, gender=gender, phone_num=phone_num)

  elif option =='2': # facebook sign in
    if (email=='' or username=='' or gender=='' or fb_id==''):
      return HttpResponse(simpleJson(3,'Error-Blank Form'))
    if User.objects.filter(email__exact=fb_email).count():
      origin = User.objects.get(email=fb_email)

      ####
      ####
      ## delete function -> remove cascading!!!!

      return HttpResponse(simpleJson(2, 'Duplicated id'))

    newUser = User(name=username, email=fb_email, gender=gender, fb_id=fb_email, phone_num=phone_num)

  else:
    return HttpResponse(simpleJson(4, 'check your options'))

  newUser.save()

  # sync operation

  if fb_friend != '':
    # friend sync from facebook's friend
    fb_friend_list = fb_friend.split(',')
    for fb in fb_friend_list:
      # friend is facebook id
      try:
        friend=User.objects.get(email=fb)
      except ObjectDoesNotExist:
        continue
      
      newUser.friend_ship.add(friend)


  if phone_contact != '':
    phone_contact_list = phone_contact.split(',')
    for contact in phone_contact_list:
      # friend is facebook id
      try:
        friend=User.objects.get(phone_num=contact)
      except ObjectDoesNotExist:
        continue
      
      newUser.friend_ship.add(friend)
    
  return HttpResponse(simpleJson(1, 'Success sign'))


def main(request):
  # input : user id.
  # output : arranger_name, next_arranger_name, candidate_num

  email = request.POST.get('email', '')

  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
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
    
  except ObjectDoesNotExist: # there is no arranger info
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

  email = request.POST.get('email', '')

  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  friend_list = User.objects.filter(friend_ship=user.id)
  if friend_list.count() < 3:
    c = {'Status' : 3, 'Log': 'You need more friends', 'Value': friend_list.count()}
    return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))
  # upgrade plan :: search friend_list, which has one more friend with target_gender
  # upgrade plan :: and then, select one as arranger, then, select his friend as candidate

  target_gender = 1
  if user.gender ==1:
    target_gender = 2

  output = []
  for friend in friend_list:
    output += User.objects.filter(friend_ship=friend.id, gender=target_gender).exclude(friend_ship=user.id)

  # remove duplicate & ex_candidate
  output = list(set(output) - set(user.ex_candidate.all()))
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
  target_email = request.POST.get('target','')
  
  if target_email == '':
    HttpResponse(simpleJson(3, 'no target friend'))

  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  target_friend = User.objects.get(email=target_email)
  user.friend_ship.add(target_friend)

  return HttpResponse(simpleJson(1, 'success'))


def pick_candidate(request):
  email = request.POST.get('email', '')

  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  c = {
        'Status' : 1, 'Log': 'success', \
        'candidate_profile': 'developing now', 'candidate_pic': user.candidate_now.profile_pic
      }
  #turn the chance OFF
  user.chance = 2
  user.save()
  # send a request !, this is asymmetric relationship.
  user.meeting_req.add(user.candidate_now)
  user.ex_candidate.add(user.candidate_now)
  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))


def view_my_friend(request):
  email = request.POST.get('email', '')
  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  user_list = []
  for idx, item in enumerate(user.friend_ship.all()):
    # using item, get name and email
    user_info = {
                  'name': item.name, 'email': item.email, 'profile_pic':item.profile_pic
                }
    user_list.append(user_info)

  c = {
        'Status' : 1, 'Log': 'success', \
        'my_friend_list': user_list , 'friend_num' : idx+1
      }

  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))


def view_friend_req(request):
  email = request.POST.get('email', '')
  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))
  
  # my send user list (get to_user using from_user)
  user_list1=user.friend_req.all()
  for idx1, item in enumerate(to_email_set):
    # using item, get name and email
    senduser = User.objects.get(id=item)
    user_info = {
                  'name': senduser.name, 'email': senduser.email, 'profile_pic':senduser.profile_pic
                }
    user_list1.append(user_info)

  # my receive user list (get from_user using to_user=me)
  user_list2 = User.objects.filter(friend_req__id=user.id)
  for idx2, item in enumerate(to_email_set):
    # using item, get name and email
    re_user = User.objects.get(id=item)
    user_info = {
                  'name': re_user.name, 'email': re_user.email, 'profile_pic':re_user.profile_pic
                }
    user_list2.append(user_info)

  c = {
        'Status' : 1, 'Log': 'success', \
        'send_list': user_list1 , 'send_num' : idx1+1, \
        'receive_list' : user_list2, 'receive_num' : idx2+1
      }

  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))


def view_meeting_req(request):
  email = request.POST.get('email', '')
  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))
  
  # my send list
  user_list1=user.meeting_req.all()
  for idx1, item in enumerate(to_email_set):
    # using item, get name and email
    senduser = User.objects.get(id=item)
    user_info = {
                  'name': senduser.name, 'email': senduser.email, 'profile_pic':senduser.profile_pic
                }
    user_list1.append(user_info)

  # my receive user list (get from_user using to_user=me)
  user_list2 = User.objects.filter(meeting_req__id=user.id)
  for idx2, item in enumerate(to_email_set):
    # using item, get name and email
    re_user = User.objects.get(id=item)
    user_info = {
                  'name': re_user.name, 'email': re_user.email, 'profile_pic':re_user.profile_pic
                }
    user_list2.append(user_info)

  c = {
        'Status' : 1, 'Log': 'success', \
        'send_list': user_list1 , 'send_num' : idx1+1, \
        'receive_list' : user_list2, 'receive_num' : idx2+1
      }

  return HttpResponse(json.dumps(c, indent=4, separators = (',', ':')))


def deny_req(request):
  # meeting_deny
  email = request.POST.get('email', '')
  target_email = request.POST.get('target_email','')
  try:
    user = User.objects.get(email__exact=email)
    target = User.objects.get(email__exact=target_email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  try:
    target = User.meeting_req.get(id=target_email.id)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(3, 'not requested'))

  target.meeting_req.remove(user)
  user.meeting_deny.add(target)

  return HttpResponse(simpleJson(1, 'success'))


def accept_req(request):
  email = request.POST.get('email', '')
  target_email = request.POST.get('target_email','')
  try:
    user = User.objects.get(email__exact=email)
    target = User.objects.get(email__exact=target_email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  try:
    target = User.meeting_req.get(id=target_email.id)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(3, 'not requested'))

  target.meeting_req.remove(user)
  user.meeting_app.add(target)

  return HttpResponse(simpleJson(1, 'success'))


def sync_friend(request):
  email = request.POST.get('email', '')
  fb_friend = request.POST.get('fb_friend','')
  phone_contact = request.POST.get('phone_contact', '')

  try:
    user = User.objects.get(email__exact=email)
  except ObjectDoesNotExist:
    return HttpResponse(simpleJson(2, 'wrong user'))

  if fb_friend != '':
    # friend sync from facebook's friend
    fb_friend_list = fb_friend.split(',')
    for fb in fb_friend_list:
      # friend is facebook id
      try:
        friend=User.objects.get(fb_id=fb)
      except ObjectDoesNotExist:
        continue
      
      user.friend_ship.add(friend)


  if phone_contact != '':
    phone_contact_list = phone_contact.split(',')
    for contact in phone_contact_list:
      # friend is facebook id
      try:
        friend=User.objects.get(phone_num=contact)
      except ObjectDoesNotExist:
        continue
      
      user.friend_ship.add(friend)
  return HttpResponse(simpleJson(1, 'success'))


def new_cycle(request):
  # this funtion will only used by admin
  # Turn all chance ON
  # And all user, get new arranger & candidate

  email = request.POST.get('adminid', '')
  password = request.POST.get('password', '')

  if email!='teeth' or password!='xltm0630@':
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

    # remove duplicate & ex_candidate
    output = list(set(output) - set(user.ex_candidate.all()))
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












