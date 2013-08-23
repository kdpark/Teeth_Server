from django.db import models

# Create your models here.
class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  friend_ship = models.ManyToManyField('self', related_name = 'user_friendship', blank = True, symmetrical = True)
  meeting_req = models.ManyToManyField('self', related_name= 'fk_meeting_req', blank=True, null=True, symmetrical = False)

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)