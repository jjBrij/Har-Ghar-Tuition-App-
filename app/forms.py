# forms.py

from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'id': 'student-name'}),
    )
    student_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Student ID', 'id': 'roll-number'}),
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Amount'}),
    )

class TutorApplicationForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    subject_expertise = forms.CharField(max_length=200, label='Subject Expertise')
    experience = forms.CharField(max_length=100, label='Experience')
    availability = forms.CharField(max_length=100, label='Availability')
    reason_to_join = forms.CharField(max_length=100, label='Why Should You Join Us?')
    resume = forms.FileField(label='Upload Your Resume (PDF only)', required=False)
