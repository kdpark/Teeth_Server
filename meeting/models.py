from django.db import models

class User(models.Model):
  name = models.CharField(max_length=65)
  password = models.TextField()
  email = models.CharField(max_length=40, unique = True)
  GenderChoice = (
      (1, 'Male'),
      (2, 'Female')
  )
  gender = models.IntegerField(choices=GenderChoice, default=1, verbose_name='Gender')
  phone_num = models.CharField(max_length=15, blank=True, null=True)
  profile_pic = models.TextField(blank=True, null=True)
  fb_id = models.CharField(max_length=15, blank=True, null=True)
  DONECHOICE = (
      (1, 'ON'),
      (2, 'OFF')
    )
  chance = models.IntegerField(choices=DONECHOICE, default=1, verbose_name='Chance')
  candidate_num = models.IntegerField(blank=True, null=True)

  jointime = models.DateTimeField(auto_now_add = True)

  arranger_now = models.ForeignKey('self', related_name='fk_arranger_now', blank = True, null=True)
  candidate_now = models.ForeignKey('self', related_name='fk_candidate_now', blank = True, null=True)
  arranger_next = models.ForeignKey('self', related_name='fk_arranger_next', blank = True, null=True)
  candidate_next = models.ForeignKey('self', related_name='fk_candidate_next', blank = True, null=True)

  friend_ship = models.ManyToManyField('self', related_name = 'user_friendship', blank = True, symmetrical = True)
  friend_req = models.ManyToManyField('self', related_name = 'user_friendreq', blank = True, null=True)
  friend_approved = models.ManyToManyField('self', related_name = 'user_approved', blank = True, null=True)

  meeting_req = models.ManyToManyField('self', related_name= 'meeting_req', blank=True, null=True)
  meeting_app = models.ManyToManyField('self', related_name = 'meeting_app', blank=True, null=True)
  meeting_deny = models.ManyToManyField('self', related_name = 'meeting_deny', blank=True, null=True)

  def __unicode__(self):
    return "%s" % self.email