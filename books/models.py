from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField()
    pdf = models.FileField(upload_to='file/')

    def summary(self):
        return self.description[:100]

    def upload_date(self):
        return self.upload_date.strftime('%b %e %Y')
