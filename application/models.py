from django.db import models

from jobposting.models import Job

# Create your models here.

class Application(models.Model):
    job = models.ForeignKey(Job)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    middle_name = models.CharField(max_length = 128)
    email_address = models.EmailField()
    address_street_1 = models.CharField(max_length = 128)
    address_street_2 = models.CharField(max_length = 128)
    address_state = models.CharField(max_length = 64)
    address_city = models.CharField(max_length = 64)
    address_zip_code = models.CharField(max_length = 14)
    phone_number = models.CharField(max_length = 16)
    resume_text = models.CharField(max_length = 4000)
    cover_letter = models.CharField(max_length = 4000)
    resume_document = models.CharField(max_length = 128)
    created_date = models.DateTimeField('date created')

    def __unicode__(self):
        return str(self.job.id)
    def __str__(self):
        return self.resume_text