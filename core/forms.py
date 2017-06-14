from django.forms import ModelForm


from core.models import User, Review


## Multiple forms for UserRegistration to allow pagination via a wizard
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


## Multiple forms for ReviewSubmission to allow pagination via a wizard
class ReviewSubmissionForm1(ModelForm):
    """Review Submission form, page 1"""
    class Meta:
        model = Review
        fields = (
            'institution', 'position', 'research_field', 'research_info',
        )

class ReviewSubmissionForm1(ModelForm):
    """Review Submission form, page 1"""
    class Meta:
        model = Review
        fields = (
            'institution', 'position', 'research_field', 'research_info',
        )

class ReviewSubmissionForm1(ModelForm):
    """Review Submission form, page 1"""
    class Meta:
        model = Review
        fields = (
            'institution', 'position', 'research_field', 'research_info',
        )