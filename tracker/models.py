from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Run(models.Model):
    UNIT_CHOICES = (
        ('km','kilometers'),
        ('miles','miles'),
    )
    date_added= models.DateTimeField(default=timezone.now)
    date_ran = models.DateTimeField(default=timezone.now)
    distance = models.FloatField()
    units = models.CharField(max_length=5,choices=UNIT_CHOICES,default="km")
    time = models.DurationField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="",blank=True)

    def __str__(self):
        return str(self.date_ran)

    def get_absolute_url(self):
        return reverse('run-detail', kwargs={'pk': self.pk})
