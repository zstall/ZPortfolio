from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Contact(models.Model):
    name_contact = models.CharField(max_length = 100)
    email_contact = models.EmailField()
    text_contact = models.TextField()
    create_date_contact = models.DateTimeField(default = timezone.now())


    def __str__(self):
        return self.name_contact
