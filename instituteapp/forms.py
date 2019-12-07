from django import forms
from multiselectfield import MultiSelectFormField

class FeedBackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your rating:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your feedback'
            }
        )
    )


class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )

    COURSES_CHOICES =(
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)

    SHIFT_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'Afternoon'),
        ('evng', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectFormField(max_length=200, choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    locations = MultiSelectFormField(max_length=200, choices=LOCATION_CHOICES)

    GENDER_CHOICE=(
        ('m','Male'),
        ('f','Female')

    )

    gender= forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICE
    )



    start_data=forms.DateField(
        widget=forms.SelectDateWidget()
    )


