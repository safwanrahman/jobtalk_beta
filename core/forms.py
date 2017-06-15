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
    """Review Submission form, page 1 (User info)"""
    class Meta:
        model = Review
        fields = (
            'institution', 'department', 'position', 'year', 'experience',
            'gender', 'ethnicity',
        )

class ReviewSubmissionForm2(ModelForm):
    """Review Submission form, page 2 (Atmosphere)"""
    class Meta:
        model = Review
        fields = (
            'supported', 'collaborative', 'tenue_rate', 'gender_ratio',
            'children', 'supported', 'hr_text', 'satisfaction', 'comment',
        )

class ReviewSubmissionForm3(ModelForm):
    """Review Submission form, page 3 (Compensation and Benefits)"""
    class Meta:
        model = Review
        fields = (
            'annual_salary', 'travel_allowance', 'pension', 'quality',
        )
