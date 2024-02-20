from django import forms
from datetime import datetime

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
         required=False, widget=forms.URLInput(attrs={"size": '50', 'placeholder': 'https://www.example.com'}) )
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
            empty_label=("Choose Year", "Choose Month", "Choose Day")))
        
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THUR'),
        (5, 'FRI')
    )
    available_days = forms.MultipleChoiceField(
        help_text='Select all days that you can work', choices = DAYS, initial = (1, 2, 3, 4, 5),
        widget=forms.CheckboxSelectMultiple)
    desired_hourly_wage = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '10.00', 'max': '100.00', 'step': '.25'}))
    cover_letter = forms.CharField(widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'}))
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true')
