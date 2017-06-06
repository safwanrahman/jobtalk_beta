# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from formtools.wizard.views import CookieWizardView

from core.forms import (ReviewForm, 
    UserRegistrationForm1, UserRegistrationForm2, UserRegistrationForm3)
from core.models import User, Review


class UserRegistrationWizard(CookieWizardView):
    # https://docs.djangoproject.com/en/1.7/ref/contrib/formtools/form-wizard/
    form_list = [UserRegistrationForm1, UserRegistrationForm2,
        UserRegistrationForm3]
    
    def done(self, form_list, **kwargs):
        return render_to_response('core/success.html')

class ReviewSubmission(CreateView):
    form_class = ReviewForm
    model = Review
    success_url = reverse_lazy('successful')


class ReviewList(ListView):
    model = Review
    context_object_name = 'review_list'
    

class ReviewDetail(DetailView):
    model = Review


def successful(request):
    return render(request, 'core/success.html')
