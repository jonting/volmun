from django.db import models
from django.template.defaultfilters import slugify


class Committee(models.Model):
    abbr = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40)
    header = models.ImageField(upload_to='header/', null=True, blank=True)
    header_x = models.SmallIntegerField(default=50)
    header_y = models.SmallIntegerField(default=50)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    background_guide = models.FileField(upload_to='documents/', null=True, blank=True)
    docket = models.FileField(upload_to='documents/', null=True, blank=True)
    dossier = models.FileField(upload_to='documents/', null=True, blank=True)
    full_crisis = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.abbr)
        super(Committee, self).save(*args, **kwargs)

    def __str__(self):
        return self.abbr


class Topic(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='topics')
    text = models.TextField()

    def __str__(self):
        return self.text
