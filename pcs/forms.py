from django import forms
from pcs.models import Volunteer, Story

class VolunteerRegistrationForm(forms.ModelForm):
    firstName = forms.CharField(max_length = 20, help_text = "First Name:")
    lastName = forms.CharField(max_length = 20, help_text = "Last Name:")
    contactNumber = forms.CharField(max_length = 11, help_text = "Contact Number:")
    postcode = forms.CharField(max_length=6, help_text = "Postcode:")
    emailAddress = forms.EmailField(help_text = "Email Address:")

    class Meta:
        model = Volunteer
        fields = ('firstName', 'lastName', 'contactNumber', 'postcode', 'emailAddress')

class StoryForm(forms.ModelForm):
    caption = forms.CharField(max_length = 500, help_text = "Caption:")
    description = forms.CharField(max_length = 500, help_text = "Description:")
    image = forms.ImageField(help_text = "Image", allow_empty_file=False)
    # userID =

    class Meta:
        model = Story
        fields = ('caption', 'description', 'image')




