from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    addet_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    autor = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    class Meta:
        db_table = 'question'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    class Meta:
        db_table = 'answer'


# Create your models here.
