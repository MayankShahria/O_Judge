from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=100)
    question_description = models.CharField(max_length=100000)
    question_input_file = models.CharField(max_length=500)
    question_output_file = models.CharField(max_length=200)

    def __str__(self):
        return self.question_name

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='documents/',default='background.gif')
    submission_status = models.CharField(max_length=50)
    submission_language = models.CharField(max_length=50)
    submission_time = models.FloatField(default=100.00)
