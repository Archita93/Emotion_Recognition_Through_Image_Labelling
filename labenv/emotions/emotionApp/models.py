from django.db import models

# Create your models here.

# class Movie(models.Model):
# 	movie_title = models.CharField(max_length=150)
# 	release_year = models.IntegerField()
# 	director = models.CharField(max_length=100)
# 	# movie_poster = models.ImageField(upload_to='images/', None=True)
# 	movie_plot = models.TextField()
	

# 	def __str__(self):
# 		return self.movie_title


from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class UploadImage(models.Model):
    caption = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):  
        return self.caption