from django.db import models

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
    has_screener = models.BooleanField()
    is_active = models.BooleanField()
    is_approved = models.BooleanField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title