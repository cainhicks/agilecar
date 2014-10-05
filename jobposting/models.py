from django.db import models
from screener.models import Screener

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 15000)
    apply_url = models.CharField(max_length = 256)
    apply_email_address = models.EmailField()
    application_count = models.IntegerField(default = 0)
    created_date = models.DateTimeField('created date')
    posted_date = models.DateTimeField('posted date')
    expire_date = models.DateTimeField('expire date')
    screener = models.ForeignKey(Screener, null = True)
    has_screener = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_approved = models.BooleanField(default = False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title