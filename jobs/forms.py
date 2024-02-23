from django import forms
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from .models import Applicant

def validate_checked(value):
    if not value:
        raise ValidationError("Required.")
    
def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )


class JobApplicationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'https://www.example.com', 'size':'50'}
        ),
        validators=[URLValidator(schemes=['http', 'https'])]
    )
    TYPE = (
        ('none', 'Please Choose'),
        ('ft', 'Full-time'),
         ('pt', 'Part-time'),
         ('contr', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices = TYPE)
    start_date = forms.DateField(
        help_text='The earliest date you can start working', 
        widget=forms.SelectDateWidget(
            years=(2024,2025),
            attrs={'style': 'width: 20%; display: inline-block; margin: 0 1%'}
            ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'})
        
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THUR'),
        (5, 'FRI')
    )
    available_days = forms.TypedMultipleChoiceField(
        help_text='Select all days that you can work', 
        coerce=int,
        choices = DAYS, initial = (1, 2, 3, 4, 5),
        widget=forms.CheckboxSelectMultiple)
    desired_hourly_wage = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '10.00', 'max': '100.00', 'step': '.25'}))
    cover_letter = forms.CharField(widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'}))
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true',
        validators=[validate_checked])
    
    class Meta:
        model = Applicant
        fields = (
            'first_name', 'last_name', 'email', 'website', 'employment_type',
            'start_date', 'available_days', 'desired_hourly_wage',
            'cover_letter', 'resume', 'confirmation', 'job')
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
            'start_date': forms.SelectDateWidget(
                attrs = {
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = range(datetime.now().year, datetime.now().year+2)
            ),
            'desired_hourly_wage': forms.NumberInput(
                attrs = {'min':'10.00', 'max':'100.00', 'step':'.25'}
            ),
            'cover_letter': forms.Textarea(attrs={'cols': '100', 'rows': '5'}),
            'resume': forms.FileInput(attrs={'accept':'application/pdf'})
        }
        error_messages = {
            'start_date': {
                'past_date': 'Please enter a future date.'
            }
        }
