from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
	caption = models.CharField(max_length = 500)
	description = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'user-images/', blank = True)
	userID = models.ForeignKey(User)
	
	def _unicode_(self):
		return self.id

