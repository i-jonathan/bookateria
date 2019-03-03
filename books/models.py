from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    downloads = models.IntegerField(default=0)
    upload_date = models.DateTimeField()
    # size = models.FloatField()
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='file/')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)

    def summary(self):
        return self.description[:100]

    def date(self):
        return self.upload_date.strftime('%b %e %Y')
    '%m %Y %-d'

    def __str__(self):
        return self.title




