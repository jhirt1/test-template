from django import forms

GENDER_CHOICES = (
    (0, 'Female'),
    (1, 'Male')
)

REGION_CHOICES = (
    (0, 'East Anglian Region'),
    (1, 'East Midlands Region'),
    (2, 'Ireland'),
    (3, 'London Region'),
    (4, 'North Region'),
    (5, 'North Western Region'),
    (6, 'Scotland'),
    (7, 'South East Region'),
    (8, 'South Region'),
    (9, 'South West Region'),
    (10, 'Wales'),
    (11, 'West Midlands Region'),
    (12, 'Yorkshire Region')
)

EDUCATION_CHOICES = (
    (0, 'A Level or Equivalent'),
    (1, 'HE Qualification'),
    (2, 'Lower Than A Level'),
    (3, 'No Formal Quals'),
    (4, 'Post Graduate Qualifications')
)

AGE_CHOICES = (
    (0, '0-35'),
    (1, '35-55'),
    (2, '55<=')
)

DISABILITY_CHOICES = (
    (0, 'False'),
    (1, 'True')
)

IMD_CHOICES = (
    (0, '0-10%'),
    (1, '10-20%'),
    (2, '20-30%'),
    (3, '30-40%'),
    (4, '40-50%'),
    (5, '50-60%'),
    (6, '60-70%'),
    (7, '70-80%'),
    (8, '80-90%'),
    (9, '90-100%')
)

# creating a form 
class InputForm(forms.Form):
 
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    region = forms.ChoiceField(choices = REGION_CHOICES)
    imd = forms.ChoiceField(choices = IMD_CHOICES)
    education = forms.ChoiceField(choices = EDUCATION_CHOICES)
    age = forms.ChoiceField(choices = AGE_CHOICES)
    disability = forms.ChoiceField(choices = DISABILITY_CHOICES)
    studied_credits = forms.IntegerField(min_value = 0, max_value = 700, initial= 0) 
