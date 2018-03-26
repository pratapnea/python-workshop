from django.db import models
# Create your models here.

#......creates tables in the Database

class Post(models.Model):			
	title = models.CharField(max_length = 150)
	body = models.TextField()
	author = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):				#providing title name to post
		return self.title

		