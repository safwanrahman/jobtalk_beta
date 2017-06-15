# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
from core.config import (Positions, ResearchFields, Genders, Ethnicity, 
    Departments, Childcare,
)


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
        null=True, blank=True,
    )
    position = models.IntegerField(choices=Positions.CHOICES,
        verbose_name='What is (or was) your position at that institution?',
        null=True, blank=True,
    )
    year = models.IntegerField(
       verbose_name='What year did your position begin?',
       null=True, blank=True,
    )
    experience = models.TextField(
        verbose_name='Describe your general experience',
        blank=True,
    )
    
    # User's identity
    gender = models.IntegerField(choices=Genders.CHOICES, 
        verbose_name='Gender',
        null=True, blank=True,
    )
    ethnicity = models.IntegerField(choices=Ethnicity.CHOICES,
        verbose_name='Ethnicity',
        null=True, blank=True,
    )
    
    # Atmosphere
    supported = models.IntegerField(
        verbose_name='How supported did you feel (1-10)?',
        null=True, blank=True,
    )
    collaborative = models.NullBooleanField(blank=True,
        verbose_name='Was it collaborative?',
    )
    tenue_rate = models.IntegerField(
        verbose_name='Estimate tenure rate',
        null=True, blank=True,
    )
    gender_ratio = models.IntegerField(
        verbose_name='Estimate gender ratio (% women faculty)',
        null=True, blank=True,
    )
    children = models.NullBooleanField(blank=True,
        verbose_name='Do you have children?'
    )
    supported = models.IntegerField(
        verbose_name='How supportive was it of having children (1-10)?',
        null=True, blank=True,
    )
    hr_text = models.TextField(
        verbose_name='Have you had to deal with HR and how did they handle it?',
        blank=True,
    )
    satisfaction = models.IntegerField(
        verbose_name='General satisfaction (1-10)',
        null=True, blank=True,
    )
    comment = models.TextField(
        verbose_name='Any additional comments?',
        blank=True,
    )
    
    # Compensation and benefits
    annual_salary = models.IntegerField(
        verbose_name='Annual salary (USD / year)',
        null=True, blank=True,
    )
    travel_allowance = models.IntegerField(
        verbose_name='Travel allowance (USD / year)',
        null=True, blank=True,    
    )
    pension = models.IntegerField(
        verbose_name='Pension/401K matching (USD / year)',
        null=True, blank=True,    
    )
    parental_leave = models.IntegerField(
        verbose_name='Parental leave (weeks)',
        null=True, blank=True,    
    )
    sick_leave = models.IntegerField(
        verbose_name='Sick leave (weeks)',
        null=True, blank=True,    
    )    
    childcare_available = models.IntegerField(
        verbose_name='Childcare available?',
        choices=Childcare.CHOICES,
        null=True, blank=True,
    )
    childcare_quality = models.IntegerField(
        verbose_name='Childcare quality (1-10)',
        null=True, blank=True,    
    )
    childcare_onsite = models.NullBooleanField(blank=True,
        verbose_name='Childcare onsite?',
    )    
    
    # Workload
    
    # Training program (students and postdocs only)

    def get_absolute_url(self):
        return reverse('review-detail', args=[self.pk])
