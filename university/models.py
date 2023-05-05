from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from organization.models import Organization

class University(models.Model):
    name = models.CharField(_("name"),max_length=100)
    address = models.CharField(_("address"),max_length=200)
    world_rank = models.IntegerField(_("world_rank"),  validators=[MinValueValidator(1),])

    def __str__(self):
        return self.name