from django.db import models

# Create your models here.
#inherance from django class

class Join(models.Model):
	email = models.EmailField()
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		#self.email is class variable because its declared in the class method
		return "%s" % (self.email) 
	#insall south
	#ensure model is synced in db
	#convert model to south with python manage.py convert_to_south appname
	#make changes to model (eg add new fields: ip_address = models.CharField(max_length=120, default='ABC'))
	#Run schemamigration: python manage.py schemamigration joins --auto
	# run python manage.py migrate