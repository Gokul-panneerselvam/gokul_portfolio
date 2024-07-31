from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields=['name','email','phone','message']
        widgets={
            'name':forms.TextInput(attrs={ 'class':'form-input','id': 'name'}),
            'email':forms.EmailInput(attrs={'class':'form-input','id': 'email'}),
            'phone':forms.NumberInput(attrs={'class':'form-input','id': 'phone'}),
            'message':forms.Textarea(attrs={'class':'form-textarea','id': 'msg'}),
        }