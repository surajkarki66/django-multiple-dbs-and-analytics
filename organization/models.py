from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    ORG_TYPES_CHOICES = [
        ('public', 'PUBLIC'),
        ('private', 'PRIVATE')
    ]
    name = models.CharField(_("name"), max_length=100)
    address = models.CharField(_("address"), max_length=200)
    org_type = models.CharField(_("org_type"), choices=ORG_TYPES_CHOICES, max_length=7)

    def __str__(self):
        return self.name
