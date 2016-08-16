from django.db import models

class Listing(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Date Published')
	email = models.CharField(max_length=200)
	price = models.CharField(max_length=20)
	body = models.CharField(max_length=1500)
	subject = models.CharField(max_length=4)
	course_number = models.CharField(max_length=4)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.title
