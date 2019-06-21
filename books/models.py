from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os
# Create your models here.


class Books(models.Model):

    def path_and_rename(self, filename):
        upload_to = 'file/'
        name = self.title + ' ' + self.author + '-bookateria.net.'
        new_name = name.replace(' ', '-') + filename.split('.')[-1]
        return os.path.join(upload_to, new_name)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    downloads = models.IntegerField(default=0, editable=False)
    upload_date = models.DateTimeField()
    size = models.FloatField(null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    pdf = models.FileField(upload_to=path_and_rename)
    uploader = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True)
    typology = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ('title', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '-' + self.author)
        if len(self.slug) >= 100:
            self.slug = self.slug[:100]
        return super(Books, self).save(*args, **kwargs)

    def megabytes(self):
        self.size = self.pdf.size
        if self.size < 1024:
            fsize = self.size
            message = str(fsize) + ' Bytes'
        elif self.size < 1048576:
            fsize = round(self.size/1024, 2)
            message = str(fsize) + ' Kb'
        else:
            fsize = round(self.size/1048576, 2)
            message = str(fsize) + ' Mb'
        return message

    def summary(self):
        return self.description[:100]

    def date(self):
        return self.upload_date.strftime('%b %d %Y')

    def __str__(self):
        return self.title


class Type(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
