# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from core.forms import UserRegistrationForm, ReviewForm
from core.models import User, Review


class UserRegistration(CreateView):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('successful')


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
