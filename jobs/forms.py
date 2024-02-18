from django import forms

class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(initial='https://', required=False)
    TYPE = (
        ('none', 'Please Choose'),
        ('ft', 'Full-time'),
         ('pt', 'Part-time'),
         ('contr', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices = TYPE)
    start_date = forms.DateField(
        help_text='The earliest date you can start working')
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THUR'),
        (5, 'FRI')
    )
    available_days = forms.MultipleChoiceField(
        help_text='Select all days that you can work', choices = DAYS)
    desired_hourly_wage = forms.IntegerField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true')
