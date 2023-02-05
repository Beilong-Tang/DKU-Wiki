from django.db import models

# Create your models here.


class Email_Code(models.Model):
    email = models.EmailField()
    code = models.IntegerField()
    