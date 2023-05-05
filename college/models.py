from django.db import models
from django.core.validators import MinValueValidator

from university.models import University



class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    university = models.BigIntegerField(validators=[MinValueValidator(1),])

    class Meta:
        app_label = 'college'

    def __str__(self):
        return self.name


class Faculty(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name