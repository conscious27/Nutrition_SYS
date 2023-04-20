from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'cholesterol_level', 'glucose_level', 'blood_pressure', 'physical_activity', 'dietary_restriction']
