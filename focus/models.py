import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

@python_2_unicode_compatible
class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256) # question: the 1st position of charfield
    def __str__(self):
        return self.profile

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('column name', max_length=256)
    intro = models.CharField('introduction', default='')
    def __str__(self):                  # print in admin & shell
        return self.name
    class Meta:                         # print in admin
        verbose_name = 'column'         # other name / one
        verbose_name_plural = 'column'  # other name / many
        ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name = 'belong to')