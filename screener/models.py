from django.db import models

from jobposting.models import Job
from application.models import Application

# Create your models here.
class Screener(models.Model):
    name = models.CharField(max_length = 128)

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(Screener, self).__init__(*args, **kwargs)

class ScreenerQuestion(models.Model):
    QUESTION_TYPES = (
                      ('ff', 'Free Form'),
                      ('mc', 'Multiple Choice')
                      )
    question_text = models.CharField(max_length = 256)
    question_type = models.CharField(max_length = 2, choices = QUESTION_TYPES)
    screener = models.ForeignKey(Screener)

class ScreenerAnswer(models.Model):
    screener_question = models.ForeignKey(ScreenerQuestion)
    answer = models.CharField(max_length = 512)
    order = models.IntegerField()

class ScreenerResponse(models.Model):
    screener_question = models.ForeignKey(ScreenerQuestion)
    response = models.CharField(max_length = 1024)
    application = models.ForeignKey(Application, null = True)
    screener = models.ForeignKey(Screener)