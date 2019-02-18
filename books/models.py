from django.db import models
from django.contrib.auth.models import User
from storages.backends import ftp
fs = ftp.FTPStorage
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.TextField()
    downloads = models.IntegerField(default=0)
    upload_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', storage=fs)
    pdf = models.FileField(upload_to='file/', storage=fs)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.description[:100]

    def date(self):
        return self.upload_date.strftime('%b %e %Y')
    '%m %Y %-d'

    def __str__(self):
        return self.title




