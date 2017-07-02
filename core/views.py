# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from formtools.wizard.views import CookieWizardView

from core.forms import ( 
    UserRegistrationForm1, UserRegistrationForm2, UserRegistrationForm3,
    ReviewSubmissionForm1, ReviewSubmissionForm2, ReviewSubmissionForm3,
)
from core.models import User, Review


class UserRegistrationWizard(CookieWizardView):
    """A view for the paginated user registration process
    
    Present multiple UserRegistrationForms using formtools.form-wizard
    """
    # https://docs.djangoproject.com/en/1.7/ref/contrib/formtools/form-wizard/
    form_list = [UserRegistrationForm1, UserRegistrationForm2,
        UserRegistrationForm3]

    # See https://django-formtools.readthedocs.io/en/latest/wizard.html#wizard-template-for-each-form
    # for instuctions on using a different template for each step
    template_name = 'core/user_registration.html'
    
    def done(self, form_list, **kwargs):
        """Save info from completed forms to database"""
        # https://stackoverflow.com/questions/14791892/saving-django-formwizard
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        
        User.objects.create_user(**data)
        
        return render_to_response('core/success.html')           


class ReviewSubmissionWizard(CookieWizardView):
    """A view for the paginated user registration process
    
    Present multiple UserRegistrationForms using formtools.form-wizard
    """
    # https://docs.djangoproject.com/en/1.7/ref/contrib/formtools/form-wizard/
    form_list = [ReviewSubmissionForm1, ReviewSubmissionForm2,
        ReviewSubmissionForm3]
    
    # See https://django-formtools.readthedocs.io/en/latest/wizard.html#wizard-template-for-each-form
    # for instuctions on using a different template for each step
    template_name = 'core/review_submission.html'
    
    def done(self, form_list, **kwargs):
        """Save info from completed forms to database"""
        # https://stackoverflow.com/questions/14791892/saving-django-formwizard
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        
        Review.objects.create(**data)
        
        return render_to_response('core/success.html')


class ReviewList(ListView):
    model = Review
    context_object_name = 'review_list'
    

class ReviewDetail(DetailView):
    model = Review


def successful(request):
    return render(request, 'core/success.html')
