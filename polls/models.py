from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# inheriting the Model from Django library


class Question(models.Model):
    # setting the fields
    ques = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date publishes")

    def __str__(self):
        return self.ques

    def is_it_recent(self):
        now = timezone.now()
        # checking if the pub date is in between day before yesterday and today
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choices(models.Model):
    # here we are specifying the relaionship between the two table and delete it it is not present in the parent one
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
