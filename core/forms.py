from django.forms import ModelForm

from core.models import User, Review


class UserRegistrationForm(ModelForm):

    class Meta:
        model = User
        exclude = ('is_superuser', 'is_active', 'is_staff', 'groups', 'user_permissions',
                   'date_joined', 'last_login', 'password')


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
