from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=30)
    description = models.TextField()
    downloads = models.IntegerField(default=0)
    upload_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='file/')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)

    def summary(self):
        return self.description[:100]

    def date(self):
        return self.upload_date.strftime('%b %e %Y')
    '%m %Y %-d'

    def __str__(self):
        return self.title




