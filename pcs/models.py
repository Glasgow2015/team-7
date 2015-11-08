from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
	caption = models.CharField(max_length = 500)
	description = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'user-images/', null=True, blank = True)
	user = models.ForeignKey(User, null=True)
	
	def _unicode_(self):
		return self.id

class Volunteer(models.Model):
	firstName = models.CharField(max_length = 20);
	lastName = models.CharField(max_length = 20);
	contactNumber = models.CharField(max_length = 11)
	postcode = models.CharField(max_length = 6)
	emailAddress = models.EmailField();

	def _unicode_(self):
		return self.id


