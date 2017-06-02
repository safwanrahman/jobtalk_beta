# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from core.config import Positions, ResearchFields, Genders, Ethnicity, Departments


class User(AbstractUser):
    institution = models.CharField(max_length=250)
    position = models.IntegerField(choices=Positions.CHOICES)
    research_field = models.IntegerField(choices=ResearchFields.CHOICES)
    research_info = models.TextField()
    career_vision = models.TextField()
    workplace_info = models.TextField()
    learn_about = models.TextField()
    gender = models.IntegerField(choices=Genders.CHOICES)
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES)


class Review(models.Model):
    institution = models.CharField(max_length=250)
    department = models.IntegerField(choices=Departments.CHOICES)
    position = models.IntegerField(choices=Positions.CHOICES)
    long = models.IntegerField(verbose_name='For how long')
    experience = models.TextField()
    gender = models.IntegerField(choices=Genders.CHOICES)
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES)
    supported = models.IntegerField(verbose_name='Do you feel supported?')
    collaborative = models.NullBooleanField(blank=True)
    tenue_rate = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    children = models.NullBooleanField(blank=True)
    supported = models.IntegerField(verbose_name='Do you feel supported?')
    hr_review = models.IntegerField(verbose_name='Have you had to deal with HR?')
    hr_text = models.TextField(verbose_name='How did they handle it?')
    satisfaction = models.IntegerField()
    comment = models.TextField()
    annual_salary = models.IntegerField()
    travel_allowance = models.IntegerField()
    pension = models.IntegerField()
    quality = models.IntegerField()
