from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = [
            'name',
            'roll_number',
            'course',
            'branch',
            'contact_number',
            'email'
        ]
