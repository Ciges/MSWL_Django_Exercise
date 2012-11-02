# PLACES PROJECT
from django.db import models

# Create your models here.

# Place model
class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=500,blank=True,null=True)
    creation_date = models.DateTimeField()
    nr_views = models.IntegerField(default=0)
    # Get name as instance description
    def __unicode__(self):
        return self.name
