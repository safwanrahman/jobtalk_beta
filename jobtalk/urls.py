"""jobtalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core.views import (UserRegistration, successful, ReviewSubmission,
    ReviewList, ReviewDetail)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', UserRegistration.as_view(), name='user-registration'),
    url(r'^reviews$', ReviewList.as_view(), name='review-list'),
    url(r'^reviews/$', ReviewList.as_view(), name='review-list'),
    url(r'^reviews/submit$', ReviewSubmission.as_view(), name='review-submission'),
    url(r'^reviews/(?P<pk>[0-9]+)/$', ReviewDetail.as_view(), name='review-detail'),
    url(r'success/', successful, name='successful'),
]
