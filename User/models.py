from django.db import models
from timezone_field import TimeZoneField
from datetime import datetime
# Create your models here.

class ActivityPeriod(models.Model):
    
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'ActivityPeriod'
    def __str__(self):
        return str(self.id)

class User(models.Model):

    id=models.CharField(primary_key=True,max_length=10)
    real_name=models.CharField(max_length=100)
    tz=TimeZoneField()
    activity_periods= models.ManyToManyField(ActivityPeriod)

    class Meta:
        verbose_name_plural = 'User'
    def __str__(self):
        return self.real_name