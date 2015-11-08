from django import forms
from pcs.models import Volunteer

class VolunteerRegistrationForm(forms.ModelForm):
    firstName = forms.CharField(max_length = 20, help_text = "First Name:")
    lastName = forms.CharField(max_length = 20, help_text = "Last Name:")
    contactNumber = forms.CharField(max_length = 11, help_text = "Contact Number:")
    postcode = forms.CharField(max_length=6, help_text = "Postcode:")
    emailAddress = forms.EmailField(help_text = "Email Address:")

    class Meta:
        model = Volunteer
        fields = ('firstName', 'lastName', 'contactNumber', 'postcode', 'emailAddress')