from django.forms import ModelForm


from core.models import User, Review


class UserRegistrationForm1(ModelForm):
    """User Registration form, page 1"""
    class Meta:
        model = User
        fields = (
            'institution', 'position', 'research_field', 'research_info',
        )


class UserRegistrationForm2(ModelForm):
    """User Registration form, page 2"""
    class Meta:
        model = User
        fields = (
            'career_vision', 'workplace_info', 'learn_about',
        )


class UserRegistrationForm3(ModelForm):
    """User Registration form, page 3"""
    class Meta:
        model = User
        fields = (
            'gender', 'ethnicity',
        )


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
