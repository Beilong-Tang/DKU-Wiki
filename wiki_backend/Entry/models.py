from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    avator = models.ImageField(upload_to='avator', null = True )

    def __str__(self) ->str:
        return self.user.username

class Entry(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE) # client(1) -> entry (many)
    content = models.TextField() # the content of the entry
    title = models.CharField(max_length=50) # the title of the entry
    tag = models.CharField(max_length=50) # the tag of the entry
    create_date = models.DateTimeField(auto_now_add=True) # the time it is created
    update_date = models.DateTimeField(auto_now=True) # the latest updated time
    def __str__(self) ->str:
        return self.title
    pass

class client_entry_updated(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    modified_time = models.DateTimeField(auto_now_add=True)
    diff=models.TextField()
    pass

