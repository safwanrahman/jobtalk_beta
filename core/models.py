# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
from core.config import Positions, ResearchFields, Genders, Ethnicity, Departments


class User(AbstractUser):
    institution = models.CharField(max_length=250, 
        verbose_name="What is your current institution?",
    )
    position = models.IntegerField(choices=Positions.CHOICES,
        verbose_name="What is your current position?",
    )
    research_field = models.IntegerField(choices=ResearchFields.CHOICES,
        verbose_name="What is your field of research?",
    )
    research_info = models.TextField(
        verbose_name="Share more about your research: ",
    )
    career_vision = models.TextField(
        verbose_name=("What is your vision for your career? "
            "Where do you want to bein 5 years, "
            "what questions do you have, etc.?"),
    )
    workplace_info = models.TextField(
        verbose_name="What would be your ideal workplace?",
    )
    learn_about = models.TextField(
        verbose_name="I'm interested in learning more about...",
    )
    gender = models.IntegerField(choices=Genders.CHOICES, 
        verbose_name='Gender',
    )
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES,
        verbose_name='Ethnicity',
    )


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
        return reverse('review-detail', args=[self.pk])
