# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

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
    gender = models.IntegerField(choices=Genders.CHOICES, verbose_name='How do you identify')
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES)


class Review(models.Model):
    institution = models.CharField(max_length=250)
    department = models.IntegerField(choices=Departments.CHOICES)
    position = models.IntegerField(choices=Positions.CHOICES)
    year = models.IntegerField(verbose_name='What year did your position begin?')
    experience = models.TextField(verbose_name='Describe your general experience')
    gender = models.IntegerField(choices=Genders.CHOICES, verbose_name='How do you identify')
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES)
    supported = models.IntegerField(verbose_name='Do you feel supported?')
    collaborative = models.NullBooleanField(blank=True)
    tenue_rate = models.IntegerField(verbose_name='Estimate tenure rate for new professors')
    gender_ratio = models.IntegerField(verbose_name='Estimate gender ratio (% women faculty)')
    children = models.IntegerField(blank=True, null=True)
    supported = models.IntegerField(verbose_name='Do you feel supported?')
    hr_text = models.TextField(verbose_name='have you had to deal with HR and how did they handle it?')
    satisfaction = models.IntegerField()
    comment = models.TextField()
    annual_salary = models.IntegerField(verbose_name='Annual salary (USD)')
    travel_allowance = models.IntegerField()
    pension = models.IntegerField()
    quality = models.IntegerField()

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.pk)])