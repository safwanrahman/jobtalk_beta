# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
from core.config import Positions, ResearchFields, Genders, Ethnicity, Departments


class User(AbstractUser):
    """Model definition of User, a user of the site.
    
    These properties define the characteristics of a typical user of the
    site, such as their current affiliation, interests, and identity.
    
    In the user registration form, users will see the `verbose_name`
    text next to the field.
    """
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
    """Model definition of Review, a review of an institution.
    
    These are submitted by Users. This encapsulates the opinions of a
    User about a certain position at an institution. Some of the fields
    may be auto-filled from the User's profile, if available.

    In the review submission, users will see the `verbose_name`
    text next to the field.
    """
    # Relationship of the User with the institution
    # These may be auto-filled from User
    institution = models.CharField(max_length=250,
        verbose_name='What institution are you reviewing?',
    )
    department = models.IntegerField(choices=Departments.CHOICES,
        verbose_name='Department',
    )
    position = models.IntegerField(choices=Positions.CHOICES,
        verbose_name='What is (or was) your position at that institution?',
    )
    year = models.IntegerField(
       verbose_name='What year did your position begin?',
    )
    experience = models.TextField(
        verbose_name='Describe your general experience',
    )
    
    # User's identity
    gender = models.IntegerField(choices=Genders.CHOICES, 
        verbose_name='Gender',
    )
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES,
        verbose_name='Ethnicity',
    )
    
    # Atmosphere
    supported = models.IntegerField(
        verbose_name='Do (or did) you feel supported?'
    )
    collaborative = models.NullBooleanField(blank=True,
        verbose_name='Did you feel this is (or was) a collaborative position?',
    )
    tenue_rate = models.IntegerField(
        verbose_name='Estimate tenure rate for new professors',
    )
    gender_ratio = models.IntegerField(
        verbose_name='Estimate gender ratio (% women faculty)',
    )
    children = models.IntegerField(blank=True, null=True,
        verbose_name='Did you have children (during your experience here)?'
    )
    supported = models.IntegerField(
        verbose_name='Do you feel supported?'
    )
    hr_text = models.TextField(
        verbose_name='Have you had to deal with HR and how did they handle it?',
    )
    satisfaction = models.IntegerField(
        verbose_name='General satisfaction (1-10)'
    )
    comment = models.TextField(
        verbose_name='Any additional comments?',
    )
    
    # Compensation and benefits
    annual_salary = models.IntegerField(
        verbose_name='Annual salary (USD)'
    )
    travel_allowance = models.IntegerField()
    pension = models.IntegerField()
    quality = models.IntegerField()
    
    # Workload
    
    # Training program (students and postdocs only)

    def get_absolute_url(self):
        return reverse('review-detail', args=[self.pk])
