from django.db import models

# Create your models here.
#inherance from django class

class Join(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		#self.email is class variable because its declared in the class method
		return "%s" % (self.email) 