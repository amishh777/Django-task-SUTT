import datetime

from django.db import models
from django.utils import timezone


# It defines the text and date for question storage and it inherits the syntax
# from Django's standard database modules.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Django uses the standard str method. It returns the question text where required.
    # It cannot be directly printed as it is just being passed
    # to another location or another code block by the str function.
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
