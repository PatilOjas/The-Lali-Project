from django.db import models

# Create your models here.
class Feedback(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(max_length=50)
	gender_CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]
	gender = models.CharField(
        max_length = 20,
        choices = gender_CHOICES,
        default = 'Others'
        )
	rating_choiice = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')]
	rate_the_session = models.CharField(
        max_length = 20,
        choices = rating_choiice,
        default = '1'
        )
	session_options = [('Yes','Yes'),('No','No')]
	was_the_session_insightful = models.CharField(
        max_length = 20,
        choices = session_options,
        default = 'Yes'
        )
	what_is_this = models.CharField(max_length=100)
	name_one_animal = models.CharField(max_length=100)
	question3 = models.CharField(max_length=100)
	question4 = models.CharField(max_length=100)
	question5 = models.CharField(max_length=100)