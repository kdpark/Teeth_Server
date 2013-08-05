from django.db import models

class User(models.Model):
	name = models.CharField(max_length=65, blank = False)
	password = models.TextField(blank = False)
	email = models.CharField(max_length=40, blank = False, unique = True)
	jointime = models.DateTimeField(auto_now = True)
	friendship = models.ManyToManyField("User", related_name = 'user_friendship', blank = 'True', symmetrical = 'True')
	friendreq = models.ManyToManyField("User", related_name = 'user_friendreq', blank = 'True')
	approved = models.ManyToManyField("User", related_name = 'user_approved', blank = 'True')

	def __unicode__(self):
		return "%s" % self.name