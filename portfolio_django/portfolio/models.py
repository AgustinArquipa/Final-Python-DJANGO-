from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Project(models.Model):
    '''
    title
    description
    image
    url
    '''
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)